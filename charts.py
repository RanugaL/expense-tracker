from matplotlib import pyplot as plt

def show_categoric_report(data,username):
        x=[]
        y=[]
        for category in data:
            x.append(category[0])
            y.append(category[1])

        plt.bar(x,y,color="mediumorchid")
        add_labels(x,y)
        plt.title(f'Expense Report for {username}')
        plt.xlabel('Category')
        plt.ylabel('Amount (Rs.)')

        # after plotting the data, format the labels
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

        plt.show()

def show_timely_report(data,year):
    x=[]
    y=[]
    for month in data:
        x.append(month[0])
        y.append(month[1])


    plt.bar(x, y, color="orange")
    add_labels(x, y)
    plt.title(f'Expense Report of {year}')
    plt.xlabel('Month')
    plt.ylabel('Amount (Rs.)')

    # after plotting the data, format the labels
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

    plt.show()


def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], f'Rs.{y[i]:.2f}', ha='center')