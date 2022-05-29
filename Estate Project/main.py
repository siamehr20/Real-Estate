import sys

if __name__ == '__main__':
    def Run_App():
        mood = input('Enter The Running Mood(0-1): ')
        from constant import RUNNNIG_MOOD
        run_func = RUNNNIG_MOOD[mood]
        run_func()
        print('s')
flag = 0
while flag != 1:
    Run_App()
    flag = int(input('Continue(0) _ Exit(1)'))
# Run_App()
