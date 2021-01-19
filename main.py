import subprocess
import time

#Timer in seconds
#Recommended 1800s or 30 min (S3 restrictions)
TIMER = 1800
is_ok = True

def main():
    #Run on CLI, and sleep
    while is_ok == True:
        print('Sync')
        subprocess.run(['python', 'sinc.py'], cwd= '.')
        print('Plotting and uploading')
        subprocess.run(['python', 'plot_dai_usd.py'], cwd= '.') ####
        print(f'Sleeping {TIMER} seconds')
        time.sleep(TIMER)

if __name__ == '__main__':
    print('Starting...')
    main()