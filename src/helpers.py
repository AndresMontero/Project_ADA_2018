# Helpers module
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt


IMG_PATH = '../assets/images/'
GRAPH_PATH = '{}graphs/'.format(IMG_PATH)
LABEL_SIZE = 18
TITLE_SIZE = 25
FIG_SIZE = (10, 6)


def neg_to_zero(quantity):
    """Function to clean negative albums

    Args:
        quantity:  quantity.
    Returns:
        new_quantity: Cleaned quantity.
    """
    
    if quantity <= 0:
        new_quantity = 0
    else:
        new_quantity = quantity

    # Round quantity to not have float quantities
    return np.rint(new_quantity)


def eq_ign_case(a, b):
    """Function to compare string ignoring the case

    Args:
        a:  string.
        b:  string.
    Returns:
        Boolean if they are equal ignoring the case
    """
    return a.str.lower() == b.str.lower()


def pretty_print(df, name, debug=False):
    print('{name} size: {size}'.format(name=name,
                                       size=len(df)))
    if debug:
        print('\nNaN count by column:\n{}'.format(df.isna().sum(axis=0)))
    display(df.head())


def not_eq_ign_case(a, b):
    """Function to compare string ignoring the case

    Args:
        a:  string.
        b:  string.
    Returns:
        Boolean if they are not equal ignoring the case
    """
    return ~eq_ign_case(a, b)


def uniq(a):
    return list(set(a))


def std_plot(plot_func, figsize=FIG_SIZE, title=None, xlabel=None, ylabel=None):
    """Wrapper function to plot.

    Args:
        title: string.
        xlabel: X axis string.
        ylabel: Y axis string.
        plot_func: callback to plot
        figsize: figure size
    """

    title_text = ''
    title_size = TITLE_SIZE

    xlabel_text = ''
    xlabel_size = LABEL_SIZE

    ylabel_text = ''
    ylabel_size = LABEL_SIZE

    if type(title) == str:
        title_size = TITLE_SIZE
        title_text = title
    elif type(title) == dict:
        title_size = title['size']
        title_text = title['text']

    if type(xlabel) == str:
        xlabel_size = LABEL_SIZE
        xlabel_text = xlabel
    elif type(xlabel) == dict:
        xlabel_size = xlabel['size']
        xlabel_size = xlabel['text']

    if type(ylabel) == str:
        ylabel_size = LABEL_SIZE
        ylabel_text = ylabel
    elif type(ylabel) == dict:
        ylabel_size = ylabel['size']
        ylabel_size = ylabel['text']

    plt.figure(figsize=figsize)

    fig = plot_func()

    plt.title(title_text, size=title_size)

    plt.xlabel(xlabel_text, size=xlabel_size)

    plt.ylabel(ylabel_text, size=ylabel_size)

    # fig.show()

    filename = title_text.lower().replace(' ', '_')

    fig.savefig('{graph}{file}'.format(graph=GRAPH_PATH,
                                       file=filename), bbox_inches='tight')
