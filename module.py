import matplotlib as mpl
import matplotlib.pyplot as plt


def barGraph(data, date, *args):
    list = []
    for i in args:
        list.append(data[i].loc[data.index == f'{date}.2019'].tolist())
    timeList = data['Time'].loc[data.index == f'{date}.2019'].tolist()
    dpi = 30
    fig = plt.figure(dpi=dpi, figsize=(40, 20))
    mpl.rcParams.update({'font.size': 50})
    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)
    xs = range(len(timeList))
    if len(args) == 1:
        plt.title(f'{args[0]} conditions for {date}.2019', fontsize=75)
        if args[0] == 'Temperature' or args[0] == 'Dew Point':
            plt.ylabel('Temperature,°C', fontsize=50)
        elif args[0] == 'Humidity':
            plt.ylabel('Humidity,%', fontsize=50)
        elif args[0] == 'Wind Speed':
            plt.ylabel('Wind Speed,mph', fontsize=50)
        elif args[0] == 'Pressure':
            plt.ylabel('Pressure,Hg', fontsize=50)
        plt.bar([x - 0.5 for x in xs], list[0], width=0.5, color='green', label=args[0])
        plt.xlabel('Time', fontsize=50)
        plt.xticks(xs, timeList, fontsize=30)
        fig.autofmt_xdate(rotation=90)
        plt.show()
        while True:
            print('Do you want to save this graph? Y/N')
            c = str(input())
            if c == 'Y':
                print('Enter the name of file:')
                file = str(input())
                fig.savefig(f'{file}.png')
                print('Picture was successfully saved!')
                break
            if c == 'N':
                break
    elif len(args) == 2:
        plt.title(f'Weather conditions for {date}.2019', fontsize=75)
        if args[0] == 'Temperature' and args[1] == 'Dew Point' or \
        args[1] == 'Temperature' and args[0] == 'Dew Point':
            plt.ylabel('Temperature,°C', fontsize=50)
            plt.bar([x - 0.5 for x in xs], list[0], width=0.3, color='green', label=args[0])
            plt.bar([x - 0.2 for x in xs], list[1], width=0.3, color='red', label=args[1])
            plt.xlabel('Time', fontsize=50)
            plt.xticks(xs, timeList, fontsize=30)
            fig.autofmt_xdate(rotation=90)
            plt.legend(loc='upper right', fontsize=30)
            plt.show()
            while True:
                print('Do you want to save this graph? Y/N')
                c = str(input())
                if c == 'Y':
                    print('Enter the name of file:')
                    file = str(input())
                    fig.savefig(f'{file}.png')
                    print('Picture was successfully saved!')
                    break
                if c == 'N':
                    break
        else:
            print('You cannot use this conditions together!')


def lineGraph(data, date, *args):
    timeList = data['Time'].loc[data.index == f'{date}.2019'].tolist()
    list = []
    for i in args:
        list.append(data[i].loc[data.index == f'{date}.2019'].tolist())
    dpi = 30
    fig = plt.figure(dpi=dpi, figsize=(40, 20))
    mpl.rcParams.update({'font.size': 50})
    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)
    xs = range(len(timeList))
    plt.xlabel('Time', fontsize=50)
    plt.xticks(xs, timeList, fontsize=30)
    fig.autofmt_xdate(rotation=90)
    if len(args) == 1:
        plt.title(f'{args[0]} conditions for {date}.2019', fontsize=75)
        if args[0] == 'Temperature' or args[0] == 'Dew Point':
            plt.ylabel('Temperature,°C', fontsize=50)
        elif args[0] == 'Humidity':
            plt.ylabel('Humidity,%', fontsize=50)
        elif args[0] == 'Wind Speed':
            plt.ylabel('Wind Speed,mph', fontsize=50)
        elif args[0] == 'Pressure':
            plt.ylabel('Pressure,Hg', fontsize=50)
        plt.plot([x - 0.5 for x in xs], list[0], color='green', linestyle='solid', label=args[0])
        plt.show()
        while True:
            print('Do you want to save this graph? Y/N')
            c = str(input())
            if c == 'Y':
                print('Enter the name of file:')
                file = str(input())
                fig.savefig(f'{file}.png')
                print('Picture was successfully saved!')
                break
            if c == 'N':
                break
    elif len(args) == 2:
        plt.title(f'Weather conditions for {date}.2019', fontsize=75)
        if args[0] == 'Temperature' and args[1] == 'Dew Point' or \
        args[1] == 'Temperature' and args[0] == 'Dew Point':
            plt.ylabel('Temperature,°C', fontsize=50)
            plt.plot(xs, list[0], color='green', linestyle='solid', label=args[0])
            plt.plot(xs, list[1], color='red', linestyle='solid', label=args[1])
            plt.legend(loc='upper right', fontsize=30)
            plt.show()
            while True:
                print('Do you want to save this graph? Y/N')
                c = str(input())
                if c == 'Y':
                    print('Enter the name of file:')
                    file = str(input())
                    fig.savefig(f'{file}.png')
                    print('Picture was successfully saved!')
                    break
                if c == 'N':
                    break
        else:
            print('You cannot use this conditions together!')







