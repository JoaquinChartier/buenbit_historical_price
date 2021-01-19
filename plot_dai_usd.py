import pandas as pd
from bokeh.plotting import figure, save, output_file
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError
from config_file import *
from bokeh.models import HoverTool, ColumnDataSource

ACCESS_KEY = ''
SECRET_KEY = ''
output_file(output_html_name_USD) #bokeh configuration

def read_credentials(read_file_name):
    #Read the .csv with AWS credentials
    df = pd.read_csv(read_file_name, header=None)
    key_string = df.iloc(0)[0].tolist()
    pass_string = df.iloc(0)[1].tolist()
    ACCESS_KEY = key_string[0].split('=')[1]
    SECRET_KEY = pass_string[0].split('=')[1]
    return ACCESS_KEY, SECRET_KEY

def make_plot(df):
    #Make the plot, save on .HTML file
    fig = figure(x_axis_label='Date', 
                y_axis_label='Price', 
                x_axis_type='datetime', 
                plot_width=1024, 
                plot_height=768)
    #datetime
    formatted_date = []
    date = df['datetime'].tolist()
    for f in date:
        formatted_date.append(datetime.strptime(f, "%Y-%m-%d %H:%M:%S"))
    #Making the source
    source = ColumnDataSource(data={
    'price': df['daiusd_price'].tolist(),
    'date' : formatted_date,
    'price_selling':df['daiusd_selling'].tolist(),
    'price_purchase':df['daiusd_purchase'].tolist()
                            })
    #Drawing the lines
    fig.line(x='date', y='price', line_width=3, color='red', source=source, legend_label='DAI/USD price')
    fig.line(x='date', y='price_selling', line_width=3, color='blue', source=source, legend_label='DAI/USD selling price')
    fig.line(x='date', y='price_purchase', line_width=3, color='green', source=source, legend_label='DAI/USD purchase price')
    #Configuring hovers
    hover = HoverTool()
    hover.tooltips = [('DAI price','$@{price}{%0.2f}'),
                        ('Date','@date{%F}'),
                        ('DAI selling price','$@{price_selling}{%0.2f}'),
                        ('DAI purchase price','$@{price_purchase}{%0.2f}')
                    ]
    hover.mode = 'vline'
    hover.formatters = {'@{price}':'printf',
                        '@date':'datetime',
                        '@{price_selling}':'printf',
                        '@{price_purchase}':'printf'}
    #Quiting toolbar
    fig.toolbar_location = None
    #Adding hovers
    fig.add_tools(hover)
    #Save
    save(obj=fig, title='Dai price - Beta')

def upload_to_aws(local_file, bucket, s3_file):
    #Upload to S3 bucket
    s3 = boto3.client('s3', 
                    aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY)

    #ContentType must be 'text/html' to can be interpreted by navigators 
    try:
        s3.upload_file(local_file, bucket, s3_file, ExtraArgs={'ACL':'public-read',
                                                               'ContentType':'text/html'})
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def read_csv(read_file_name):
    #Read the dataset
    df = pd.read_csv(read_file_name)
    return df

if __name__ == '__main__':
    ACCESS_KEY, SECRET_KEY = read_credentials('rootkey.csv')
    df = read_csv(out_file_name)
    make_plot(df)
    upload_to_aws(output_html_name_USD, bucket, output_html_name_USD)