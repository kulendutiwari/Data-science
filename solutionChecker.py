{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing libraries\n",
    "import pandas as pd\n",
    "import numpy as np                     # For mathematical calculations\n",
    "import seaborn as sns                  # For data visualization\n",
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sn                   # For plotting graphs\n",
    "%matplotlib inline\n",
    "import warnings                        # To ignore any warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading the data\n",
    "train = pd.read_csv('train.csv')\n",
    "test = pd.read_csv('test.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['ID', 'age', 'job', 'marital', 'education', 'default', 'balance',\n",
       "       'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign',\n",
       "       'pdays', 'previous', 'poutcome', 'subscribed'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['ID', 'age', 'job', 'marital', 'education', 'default', 'balance',\n",
       "       'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign',\n",
       "       'pdays', 'previous', 'poutcome'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((31647, 18), (13564, 17))"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape, test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ID             int64\n",
       "age            int64\n",
       "job           object\n",
       "marital       object\n",
       "education     object\n",
       "default       object\n",
       "balance        int64\n",
       "housing       object\n",
       "loan          object\n",
       "contact       object\n",
       "day            int64\n",
       "month         object\n",
       "duration       int64\n",
       "campaign       int64\n",
       "pdays          int64\n",
       "previous       int64\n",
       "poutcome      object\n",
       "subscribed    object\n",
       "dtype: object"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print data types for each variable\n",
    "train.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>age</th>\n",
       "      <th>job</th>\n",
       "      <th>marital</th>\n",
       "      <th>education</th>\n",
       "      <th>default</th>\n",
       "      <th>balance</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>subscribed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>26110</td>\n",
       "      <td>56</td>\n",
       "      <td>admin.</td>\n",
       "      <td>married</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>1933</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>telephone</td>\n",
       "      <td>19</td>\n",
       "      <td>nov</td>\n",
       "      <td>44</td>\n",
       "      <td>2</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>40576</td>\n",
       "      <td>31</td>\n",
       "      <td>unknown</td>\n",
       "      <td>married</td>\n",
       "      <td>secondary</td>\n",
       "      <td>no</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>20</td>\n",
       "      <td>jul</td>\n",
       "      <td>91</td>\n",
       "      <td>2</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>15320</td>\n",
       "      <td>27</td>\n",
       "      <td>services</td>\n",
       "      <td>married</td>\n",
       "      <td>secondary</td>\n",
       "      <td>no</td>\n",
       "      <td>891</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>18</td>\n",
       "      <td>jul</td>\n",
       "      <td>240</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>43962</td>\n",
       "      <td>57</td>\n",
       "      <td>management</td>\n",
       "      <td>divorced</td>\n",
       "      <td>tertiary</td>\n",
       "      <td>no</td>\n",
       "      <td>3287</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>22</td>\n",
       "      <td>jun</td>\n",
       "      <td>867</td>\n",
       "      <td>1</td>\n",
       "      <td>84</td>\n",
       "      <td>3</td>\n",
       "      <td>success</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>29842</td>\n",
       "      <td>31</td>\n",
       "      <td>technician</td>\n",
       "      <td>married</td>\n",
       "      <td>secondary</td>\n",
       "      <td>no</td>\n",
       "      <td>119</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>4</td>\n",
       "      <td>feb</td>\n",
       "      <td>380</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      ID  age         job   marital  education default  balance housing loan  \\\n",
       "0  26110   56      admin.   married    unknown      no     1933      no   no   \n",
       "1  40576   31     unknown   married  secondary      no        3      no   no   \n",
       "2  15320   27    services   married  secondary      no      891     yes   no   \n",
       "3  43962   57  management  divorced   tertiary      no     3287      no   no   \n",
       "4  29842   31  technician   married  secondary      no      119     yes   no   \n",
       "\n",
       "     contact  day month  duration  campaign  pdays  previous poutcome  \\\n",
       "0  telephone   19   nov        44         2     -1         0  unknown   \n",
       "1   cellular   20   jul        91         2     -1         0  unknown   \n",
       "2   cellular   18   jul       240         1     -1         0  unknown   \n",
       "3   cellular   22   jun       867         1     84         3  success   \n",
       "4   cellular    4   feb       380         1     -1         0  unknown   \n",
       "\n",
       "  subscribed  \n",
       "0         no  \n",
       "1         no  \n",
       "2         no  \n",
       "3        yes  \n",
       "4         no  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#printing first five rows of the dataset\n",
    "train.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Univariate Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     27932\n",
       "yes     3715\n",
       "Name: subscribed, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['subscribed'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     0.882611\n",
       "yes    0.117389\n",
       "Name: subscribed, dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Normalize can be set to True to print proportions instead of number \n",
    "train['subscribed'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1eecbc8e320>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plotting the bar plot of frequencies\n",
    "train['subscribed'].value_counts().plot.bar()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "So, 3715 users out of total 31647 have subscribed which is around 12%. Let's now explore the variables to have a better understanding of the dataset. We will first explore the variables individually using univariate analysis, then we will look at the relation between various independent variables and the target variable. We will also look at the correlation plot to see which variables affects the target variable most.\n",
    "\n",
    "Let's first look  at the distribution of age variable to see how many people belongs to a particular age group."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1eecbf9c8d0>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAEKCAYAAAD+XoUoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvnQurowAAIABJREFUeJzt3Xt8nGWd9/HPb2ZyTppzQ2lT2jRtoS21QGg5ykkE1AURWIs+K4/LyrKK7q6Pu4u7L11lj6yreFwVhZXFVUA8VUABKaCcSltOpec0pW16yLk5Nef8nj9mCjEkzbRNcs9kvu/XK6+ZueeazC/Tu9+55prrvm5zd0REJDWEgi5AREQmj0JfRCSFKPRFRFKIQl9EJIUo9EVEUohCX0QkhSj0RURSiEJfRCSFKPRFRFJIJOgChispKfE5c+YEXYaISFJZv359o7uXjtUu4UJ/zpw5rFu3LugyRESSipntiqedhndERFJIXKFvZpeb2VYzqzazW0e4P8PM7o/dv8bM5gy5b6mZPW9mG81sg5lljl/5IiJyNMYMfTMLA98CrgAWAdeb2aJhzW4EWty9ErgDuD322AjwQ+Bmd18MXAj0jVv1IiJyVOLp6S8Hqt29xt17gfuAq4a1uQq4J3b9QeASMzPg3cBr7v4qgLs3ufvA+JQuIiJHK57QnwnsGXK7NrZtxDbu3g+0AsXAAsDN7FEze8nM/nakJzCzm8xsnZmta2hoONq/QURE4hRP6NsI24afeWW0NhHgPODDscurzeyStzV0v9Pdq9y9qrR0zBlHIiJyjOIJ/VqgfMjtWcC+0drExvHzgebY9qfdvdHdDwGPAKcfb9EiInJs4gn9tcB8M5trZunASmDVsDargBti168FVnv0PIyPAkvNLDv2ZnABsGl8ShcRkaM15sFZ7t5vZrcQDfAwcLe7bzSz24B17r4KuAu418yqifbwV8Ye22JmXyH6xuHAI+7+8AT9LSIiMgZLtBOjV1VVuY7IPXY/WrP7bds+tGJ2AJWIyGQys/XuXjVWOx2RKyKSQhT6IiIpRKEvIpJCFPoiIilEoS8ikkIU+iIiKUShLyKSQhT6IiIpRKEvIpJCFPoiIilEoS8ikkIU+iIiKUShLyKSQhT6IiIpRKEvIpJCFPoiIilEoS8ikkIU+iIiKUShLyKSQhT6IiIpRKEvIpJCIkEXIMH50Zrdb9v2oRWzA6hERCaLevoiIilEoS8ikkIU+iIiKUShLyKSQuIKfTO73My2mlm1md06wv0ZZnZ/7P41ZjYntn2OmXWZ2Suxn++Mb/kiInI0xpy9Y2Zh4FvApUAtsNbMVrn7piHNbgRa3L3SzFYCtwMfjN23w92XjXPdIiJyDOLp6S8Hqt29xt17gfuAq4a1uQq4J3b9QeASM7PxK1NERMZDPKE/E9gz5HZtbNuIbdy9H2gFimP3zTWzl83saTM7/zjrFRGR4xDPwVkj9dg9zjb7gdnu3mRmZwC/MLPF7t72Bw82uwm4CWD2bB0cJCIyUeLp6dcC5UNuzwL2jdbGzCJAPtDs7j3u3gTg7uuBHcCC4U/g7ne6e5W7V5WWlh79XyEiInGJJ/TXAvPNbK6ZpQMrgVXD2qwCbohdvxZY7e5uZqWxL4IxswpgPlAzPqWLiMjRGnN4x937zewW4FEgDNzt7hvN7DZgnbuvAu4C7jWzaqCZ6BsDwDuB28ysHxgAbnb35on4Q0REZGxxLbjm7o8Ajwzb9vkh17uB60Z43E+Bnx5njSIiMk50RK6ISApR6IuIpBCFvohIClHoi4ikEIW+iEgKUeiLiKQQhb6ISApR6IuIpBCFvohIClHoi4ikEIW+iEgKUeiLiKQQhb6ISApR6IuIpJC4llaW1PGjNbtH3P6hFTqNpchUoJ6+iEgKUehPQV29Azxf08S+g11BlyIiCUbDO1PI4KCzdmczj246wKHeAQBOnZnPeZUlzC7ODrg6EUkE6ulPIV9fvZ2fv7KX6XkZ3HR+BRcuLGXLgTau/q9n2d10KOjyRCQBKPSniI6efu5+ZieLZkzjY+dXMKckh3cvOoFbLppP/6Dz0R+8SOuhvqDLFJGAKfSniPte3E1bdz8XLCjFzN7cXpqXwZ1/cga7mw9x8w/X0zcwGGCVIhI0jekngbGmUfYNDHLXMztZMbeI8qK3j92vqCjm9muW8ukHXuXbT+3gU5fMn9B6RSRxqac/Bfzq1X3sb+3m5gvmjdrmA6fP4sp3nMg3Vm9n8/62SaxORBKJQn8KuOuZnSwsy+PChaVHbPfFKxeTn5XOZ37yqoZ5RFKUQj/J1bd1s3FfGx84feYfjOWPpDAnnX+5egkb97Xx3ad3TFKFIpJIFPpJ7vmaJgDOrSyJq/1li0/giiUn8K0nd9Dapdk8IqkmrtA3s8vNbKuZVZvZrSPcn2Fm98fuX2Nmc4bdP9vMOszsM+NTthz2XHUT+VlpnDJjWtyP+fv3nMKAO49tPDCBlYlIIhoz9M0sDHwLuAJYBFxvZouGNbsRaHH3SuAO4PZh998B/Pr4y5XhnqtpZMXcIsKhIw/tDFVelM2fnTeXl/ccZE+zDtoSSSXx9PSXA9XuXuPuvcB9wFXD2lwF3BO7/iBwicUGmM3s/UANsHF8SpbD9jQfYk9zF+fMKz7qx378okpyMyI8vGE/7j4B1YlIIoon9GcCe4bcro1tG7GNu/cDrUCxmeUAfwd88fhLleEOj+efE+d4/lC5GREuPaWM3c2H2FbXPt6liUiCiif0Rxo3GN41HK3NF4E73L3jiE9gdpOZrTOzdQ0NDXGUJADP72iiJDed+dNzj+nxp51UQEF2Gqu31Ku3L5Ii4gn9WqB8yO1ZwL7R2phZBMgHmoEVwH+Y2RvAXwF/b2a3DH8Cd7/T3avcvaq09MhzzSXK3XluRyNnzysZc6rmaCKhEBcumM6eli6q64/4viwiU0Q8ob8WmG9mc80sHVgJrBrWZhVwQ+z6tcBqjzrf3ee4+xzgq8C/uvs3x6n2lNbY0UtdWw9nVxz9eP5Qp59UQH5WGk+oty+SEsYM/dgY/S3Ao8Bm4AF332hmt5nZlbFmdxEdw68GPg28bVqnjK/dsVk3y+cWHtfviYRCXLCglN3Nh9jR0DkepYlIAotrwTV3fwR4ZNi2zw+53g1cN8bv+MIx1Cej2NfaRVZamLklxzaeP1TVSYWs3lLPM9UNVB7j9wMikhx0RG6S2n+wi1Nm5B3V/PzRRMIhzqooYltdB/Vt3eNQnYgkKi2tnIQG3dnf2s3588fvS+/lc4t5amsDz+5o4urThs/IHdlYSz6LSOJRTz8JtXT20tM/yOIT4196YSy5GRGWlRfw8u4WOnv6x+33ikhiUegnoX2t0SGYReMY+hBdtK1/0HnxjeZx/b0ikjgU+klo/8EuQgYLyvLG9feWTctk/vRcXtjRRL/W2xeZkhT6SWh/azfT8zLJTAuP++8+t7KE9p5+XtvbOu6/W0SCp9BPQvtau5iRnzkhv3v+9Fym52XwbHWjDtYSmYIU+kmmvbuP9u5+TizImpDfb2acW1nC/tZudjbqYC2RqUahn2T2x77EnaiePsCy8gKy08M8U904Yc8hIsFQ6CeZ/Qe7AJiRPzE9fYC0cIgVc4vZeqCdxo6eCXseEZl8Cv0ks6+1m8LsNLLSx/9L3KHOqigiFDKe26HevshUotBPMnVt3Zwwgb38w/Iy03jHrALW72rhUK8O1hKZKhT6SaR/cJDGjh7KpmVMyvOdW1lM34Cz9o2WSXk+EZl4Cv0k0tjRy6BDWd7EfYk71Iz8LCpKc3h+RyN9OlhLZEpQ6CeRutgKmGXTJif0Ac6rLKGtu5+HX9s/ac8pIhNHoZ9E6tq6CRmU5KVP2nMuKMtjel4G31i9XUsziEwBCv0kUtfWQ0luBpHQ5P2zhcy4dFEZOxo6+elLtZP2vCIyMRT6SaSurXtSh3YOWzRjGsvKC/jqb7fT3Tcw6c8vIuNHoZ8kevsHaensnbSZO0OZGX93+cnsb+3m3ud3Tfrzi8j4UegniYb2HhyYPkkzd4Y7e14xFywo5ZtPVtPc2RtIDSJy/HS6xCRxeObOCQEM7xz2D+89hfd87ffc/ust3H7t0qN6rE6tKJIY1NNPEnVt3URCRlHu5M3cGW5BWR43nj+X+9ftYf0unV1LJBkp9JNEXXs30/MyCJkFWsenLp7PifmZ/MPPX2dgUOvtiyQbDe8kibq2HipKcoIug5yMCJ//o8Xc/MP1vFDTxLmVJeP+HBoKEpk46uknga7eAVq7+gKZrjmSyxaXcdHCUh7fXEdrV1/Q5YjIUVDoJ4H69uiXuNMDmK45EjPji1cuYXDQeWSDlmcQSSZxhb6ZXW5mW82s2sxuHeH+DDO7P3b/GjObE9u+3Mxeif28amZXj2/5qaGuLXoik0Tp6QPMLs7mwoWlbNjbyva69qDLEZE4jRn6ZhYGvgVcASwCrjezRcOa3Qi0uHslcAdwe2z760CVuy8DLge+a2b6HuEo1bV1kx4JUZCVFnQpf+Cd80spzknnl6/u0yqcIkkinp7+cqDa3WvcvRe4D7hqWJurgHti1x8ELjEzc/dD7n74DByZgKZ7HIO6tm7K8jKwgGfuDBcJh3j/aTNp7uzlyS31QZcjInGIJ/RnAnuG3K6NbRuxTSzkW4FiADNbYWYbgQ3AzUPeBCROQa25E495pbmcPruQ321v4EDspO0ikrjiCf2RupfDe+yjtnH3Ne6+GDgT+KyZvS29zOwmM1tnZusaGhriKCl1NHb00Nk7kLChD/CeJSeQmRbm5y/XMuj6MCeSyOIJ/VqgfMjtWcC+0drExuzzgT84ZNPdNwOdwJLhT+Dud7p7lbtXlZaWxl99CtgW+5I0kUM/OyPCe0+dwZ6WLtbs1JG6IoksntBfC8w3s7lmlg6sBFYNa7MKuCF2/Vpgtbt77DERADM7CVgIvDEulaeIbQcOh35iTNcczbLyAiqn5/LYxgMa5hFJYGPOpHH3fjO7BXgUCAN3u/tGM7sNWOfuq4C7gHvNrJpoD39l7OHnAbeaWR8wCHzc3Rsn4g+ZqrbWdZCdHiY34+3/VKMduRoEM+P9y2bytSe28Y+rXue7f1IVdEkiMoK4pk+6+yPAI8O2fX7I9W7guhEedy9w73HWmNK21bVTNi0z4WbujKQoJ51LTi7jNxsP8JvX93P5khlBlyQiw+iI3ATm7mw70J7wQztDnVtZwpKZ0/jszzZomEckASn0E9iBtm7ae/oDO3HKsQiHjK+tPI3uvkH++v5XtBKnSIJR6CewrQcSf+bOSOaV5vLFqxbzfE0T33l6R9DliMgQWhIhgW1Nkpk7I7nujFn8fnsjX35sKwvK8ibsebQMs8jRUU8/gW3c18bMgiyy05PvvdnMuP2aUzl1Zj6f/PFL7Gk+FHRJIoJ6+gnt9X2tLD5x2nH/nqCmdmanR/j+DWfygW8/yz3Pv8HHzq9IuqEqkalGPf0E1dHTz87GTpbMzA+6lONSmpfBPR9dTtiM7zy9480jjEUkGAr9BLV5fxvusGTm8ff0g1ZRmstfXDiPopx07nnuDZ7aWk+/lmIWCYRCP0FtqG0FSPqe/mEF2enc9M4KFs/M57FNddzx2228VntQUzpFJpnG9BPU6/tamZ6XkVRz9MeSEQnzoeWz2V7fzq83HOC+tXt4bkcTN5wzhw+eWT7iUhPjSTN9RBT6CWvj3rYp08sfbv70POZdnMvGfW1sr2vnnx7axDdXb+fPL5jHR84+KejyRKY0De8koK7eAbbXt7NkHGbuJKqQGafOzOfBvziHX3ziXJbOKuDff72FS778NG80dgZdnsiUpdBPQJsPtDHosHiK9vSHW1ZewD1/upwH/vxs0iMhvv9MDU9trdcJWUQmgEI/AW3cO7W+xI3X8rlFPPTJ81h8YvTL3p+9tFfBLzLONKafgF7f20Zhdhon5k+dL3HjlZeZxsozyynNy2D1lnrcnWvOmEUoCZaWFkkGCv2AHGkmyYa9rSyZmZ8Ua+hPBDPjXaeUETLjt5vrcODaM2YFXZbIlKDhnQRzqLefrXXtLJ2VWkM7I7n45Om8e1EZr+w5yC9f2YtrqEfkuCn0E8yre1oZGHSqTioKupSEcOHC6Vy4sJS1b7Rw20ObFPwix0nDOwnmpd0tAJw2uyDgShLHpaeU0dc/yH8/+wbZ6WH+5rKTgy5JJGkp9BPM+l0tVE7PpSA7PehSEoaZ8Z5TZzC7OIdvPbmD7PQIn7iockKfU0fvylSl0E8gg+68tLuFyxadEHQpCcfM+Jf3L6G7b4AvPboVd5/w4BeZihT6CaSxo4eDh/o4Y05h0KUkpFDI+NK1S3F3/vOxbexp7mLJzHzCodSc5SRyLBT6CWR3U/TsUmecpNAfTSQc4it/vIxZhdl888lq1u1q5rqqcqZlpk3K84807KMhH0kmCv0Esqv5EAXZaVSU5ARdytsEdfatkYRCxmcuW8hJxdl89mcb+PoT2/nAabNYNIXXKhIZL5qymUB2Nx3ijNmFKXtQ1tG6rqqcWy6qpCArjR+u2cWP1uyi5VBv0GWJJDSFfoI41NNPQ0cPp2to56hMn5bJzRfO45JTprO1rp07Ht/GY5sO0NrVF3RpIglJoZ8gdjdrPP9YRUIhLjm5jL9+1wIWnTiNp7Y2cN7tq/nGE9vp6OkPujyRhBJX6JvZ5Wa21cyqzezWEe7PMLP7Y/evMbM5se2Xmtl6M9sQu7x4fMufOmoaO4mEjGXlOijrWBVkp7PyzNl88uJKzqoo5suPb+P821fznad30NU7EHR5IglhzNA3szDwLeAKYBFwvZktGtbsRqDF3SuBO4DbY9sbgT9y91OBG4B7x6vwqWZnYyflRdlkpoWDLiXpzcjP4nsfqeKXf3Bylqd4tfaglnGQlBdPT385UO3uNe7eC9wHXDWszVXAPbHrDwKXmJm5+8vuvi+2fSOQaWYZ41H4VNLdN8C+g13MTcBZO8nsHbGTs9x/01kU5qRz/9o9fO/3NdS3dQddmkhg4gn9mcCeIbdrY9tGbOPu/UArUDyszTXAy+7eM/wJzOwmM1tnZusaGhrirX3KeKOpEweF/gRZUVHMqlvO4+rTZlLX1sM3nqzmic119A8MBl2ayKSLZ57+SPMHh39GPmIbM1tMdMjn3SM9gbvfCdwJUFVVlXKfv3c2dhIOGbOLsoMuZcoKh4wz5xRxyoxpPPTaPp7YUs+Gva1cfdrw/ovI1BZPT78WKB9yexawb7Q2ZhYB8oHm2O1ZwM+Bj7j7juMteCra2dhJeWE2aWFNpppouRkRVp45mxvOnkNv/yB3/q6Gz/3iddq7NcVTUkM8KbMWmG9mc80sHVgJrBrWZhXRL2oBrgVWu7ubWQHwMPBZd392vIqeSrr7BtjbovH8ybbwhDz+8l3zOWdeMT9cs4tLv/I7Ht9UF3RZIhNuzNCPjdHfAjwKbAYecPeNZnabmV0Za3YXUGxm1cCngcPTOm8BKoHPmdkrsZ/p4/5XJLFdsfH8ilKF/mTLiIR579IT+fnHz6UgO42P/c86Pv6/66lv1xe9MnXFtfaOuz8CPDJs2+eHXO8Grhvhcf8M/PNx1jilHR7PLy/UeH5QlpUX8KtPnsedv6vha09s55ntjZw3v5QVc4s05CZTjvbogNU0djKrMIv0iP4pgpQWDvGJiyp59K/eyTvKC3hkw36+/NhWnq9p0iwfmVKUNAE6PD+/oiQ36FIkZm5JDvfeuII/O38uRTnp/OrVfXz58W28uLOZgcGUm1gmU5CWVg7QrqZOBn3qjecn0jLMx6qiJJePnZ/DjoZOHt90gF+8spent9Vz8cllLCsv0IlbJGkp9ANU06D5+YnMzKicnsu80nlsq2vn8c11/PSlWl6oaeL65bMpytF5jCX5KPQDVKP5+UnxqcDMWHjCNBaU5bFhbyu/eGUv31i9nWtOn8WSmflBlydyVFI3bQL25nj+FBvamcrMjKWzCvjkRfMpzcvgRy/uZtO+1qDLEjkqCv2AvNEYm5+vg7KSTmFOOh87v4JZhVk8sL6WrQfagy5JJG4K/YAcXj+/XOP5SSktHOLDK04iIxLiY/+zjpZOnaZRkoNCPyA1jR2UF6X2eH6yy89K48MrTmJ/axdfemxr0OWIxEWJE4DWrj72H+zW0M4UMLsomz+uKucn6/aw92BX0OWIjEmhH4AXdzZH18/Xl7hTwscvqgTgO09pEVlJfAr9ALxQ0xQdz9d6O1PCzIIsrj1jFvev3cOBVi3WJolN8/QD8EJNE7NHGc9Phnnr8nYfv7CSn6yr5TtP7+ALVy4OuhyRUamnP8kOHupl0/42zc+fYsqLsrly2Yn8ZN0euvsGgi5HZFTq6U+yF3c24w5ztcjaUUv0T0FXnzaTn720l6e3NXDZ4hOCLkdkROrpT7Lna5rITAtRXpgVdCkyzs6uKKYwO42HX9sfdCkio1LoT7IXapo546RCIpqfP+VEwiEuW3wCT2yu0xCPJCwlzyRq6exl8/42zppbHHQpMkHec+oMOnsHeHpbQ9CliIxIY/qTaM3OZgDOnlfMtrqOgKuZ2oIa/z97XjEFsSEejetLIlJPfxK9UNNEVlqYpbMKgi5FJkhaOMTlGuKRBKbQn0Qv1DRRNadQ58Od4q6IDfE8t6Mx6FJE3kbpM0maO3vZcqCdsyo0nj/VrZhbREYkxDPbm4IuReRtNKY/SdbURAPgrIqigCuR4cZ7/D8zLUzVnEKerVZPXxKPevqTROP5qeXcyhK21rVT3661eCSxKPQnyfOx8Xytn58azqssAeD5HRrikcSi4Z1J0NjRw7a6Dt5/2sygS5EJMNLw0KA70zIjPFvdyFXL9O8uiSOubqeZXW5mW82s2sxuHeH+DDO7P3b/GjObE9tebGZPmlmHmX1zfEtPHi/G5ufrS9zUETLjnHklPLO9EXcPuhyRN43Z0zezMPAt4FKgFlhrZqvcfdOQZjcCLe5eaWYrgduBDwLdwOeAJbGflPT8jiay08OcOjM/6FJkEqVHQuxr7eYbq6spyc0A4EMrZgdclaS6eHr6y4Fqd69x917gPuCqYW2uAu6JXX8QuMTMzN073f0ZouGfsqLj+UUaz08xlaXRlVR3NOjoa0kc8aTQTGDPkNu1sW0jtnH3fqAV0FgGsPdgF9X1HbxzfknQpcgkK85NJz8rjep6hb4kjnhC30bYNnyQMp42oz+B2U1mts7M1jU0TK2Fqp7eGv17LlxYGnAlMtnMjIqSHHY2djKocX1JEPGEfi1QPuT2LGDfaG3MLALkA83xFuHud7p7lbtXlZZOrXB8els9MwuymFeqk6akoorSXA71DlDf3hN0KSJAfKG/FphvZnPNLB1YCawa1mYVcEPs+rXAateUBXr7B3m2uokLFpZiNtKHIZnqKkqip8XcqXF9SRBjhn5sjP4W4FFgM/CAu280s9vM7MpYs7uAYjOrBj4NvDmt08zeAL4C/F8zqzWzReP8NySsl3a30NHTzwULptanF4lfYU46Bdlp1DR2Bl2KCBDnwVnu/gjwyLBtnx9yvRu4bpTHzjmO+pLaU1sbiISMcyv1JW4qqyjJZcuBNo3rS0LQHMIJ9PS2BqrmFJKboQOfU1lFSQ6Hegeoa0vpmcuSIBT6E6SurZvN+9u4cOH0oEuRgM0tjY3ra4hHEoBCf4I8tqkOgItPVuinusLsdAqz06hpUOhL8DTuMEF+9eo+5k/PZUFZXmDna5XEUVGSy6b9bQwOOqGQZnJJcBT64+hwuLd29bF2ZzOXnDJdgS8AzJuew/rdLWzY28o7ynVOBQmOhncmwOt7W3Fg6Uz955ao+dPzMODJrfVBlyIpTqE/AV6rPciJ+ZmU5GUEXYokiJyMCLMKs3hy69RaZkSSj0J/nLV09rKnpYtTdVpEGWbhCXm8VnuQxg4tySDBUeiPsw17WwFYqrXzZZiFZdNwh99tU29fgqPQH0eD7qx9o5nZRdkU5qQHXY4kmBkFmZTkZmiIRwKl0B9HWw+009TZyznzdCoBebuQGRcuLOV32xroHxgMuhxJUQr9cfTsjkbys9JYfKKGdmRkF588ndauPl7ZczDoUiRFKfTHyeb9bdQ0dHJWRTFhHXwjozhvfgnp4RAPvbY/6FIkRSn0x8ndz+wkLWycOacw6FIkgU3LTOOyJSfws5dq6e4bCLocSUEK/XFQ23KIX76yj9PKC8lO10HOcmTXLy+nrbufh9XblwAo9MfBvz2yhVAILtB5cCUOZ1cUU1GSw49f1BIdMvkU+sfpuR2NPLxhP39xQSWF2ZqmKWMzM65fPpt1u1rYVtcedDmSYhT6x6F/YJDbfrWJmQVZ/PkFFUGXI0nkmjNmkR4OaUE+mXQK/ePwvd/vZMuBdj73vlPITAsHXY4kkaKcdN63dAY/fnE3NTppukwihf4x+v32Br706Bbee+oMLlt8QtDlSBL6uytOJjMtzN88+BoDgzp/rkwOhf4x2N10iFt+9DLzp+fxH9cuxUzz8uXolU3L5AtXLmL9rhbufmZn0OVIilDoH6X9rV189Acv4u7c+ZEzyNFJz+U4vH/ZTN51ShlfemyrFmKTSaHQPwrV9R1c81/PUdfWw50fqeKk4pygS5IkZ2b82wdOZW5xDjf894t85fFtGuqRCaXQj9MTm+u47jvP0Tvg3HfTWZxVoUXVZHyU5mVw/fLZnFZeyNef2M7yf/ktf/qDtWza10ZvvxZmk/GlsYkx3PX7nTy8YT8v7W7hhGmZfHjFbF6rbeW12tagS5MpJD0S4tozZrGgLJcXdzbz5JZ6Vm+pJxIyZhdnMyM/k+KcDIpz09nb0kVuRoTcjAg5GRFyMyPceN7cEWeQ/e8Lu+gbcHoHBunrH6RnYJDLFpdhGOmREEU56RRkpelk7SlEoT+KQ7393PPcLr7+xHZ6+ge4aGEpF508nUhIH45k4iydVcDSWQW0dfdRNi2DHfWd7GjooL69h1drD9LU0UtHT//bHvelR7eSmRYiKy1MRiRM78AgXb0DdI2wvs/Xn9j+B7dDBoXZ6YRDRm5mhGmZaUzLjDAtK433nDqDguw08jLSyMuMvsHkZUZID4c0gSFJxRX6ZnY58DV2VO6pAAAInklEQVQgDHzf3f992P0ZwP8AZwBNwAfd/Y3YfZ8FbgQGgE+5+6PjVv0EqG05xI/W7Ob+tXto6uxlYVkely4q48SCrKBLkykg3oOxpmWmcfVps0a87wfPvkFnbz8d3f109vTT0dPPvOm5HDzUS3ffID39A6SFQ2Snh6mu7yQ9EiItbGREwqRHQlywoBRwevoHae7spbmzl6bOXl7dc5CO7n52NXXS1t3PwKAfcTXQcMiiP2ZEwm9dz0oPk5MeIScjTNWcIopy0inKSac4J53C2GVRTjq5GRG9cQTA3I/8pZGZhYFtwKVALbAWuN7dNw1p83FgqbvfbGYrgavd/YNmtgj4MbAcOBH4LbDA3UddXrCqqsrXrVt3nH9W/NydPc1drN5Sx282HuDFnc0AXHxyGTdfUMG2Oh04I4nvQytmj7j9WI/4dXe6egc4d34JrV19tHf309ETvWzv7mf9rhYGBp2BQac/djkwOEj/oNPdN0BnzwAdPf109w3QM8r3EuGQkZMeJis9TFZamMrpuUzLSiM/K41pmdHLopx0SnIzKMmLXhZlp2soahRmtt7dq8ZsF0fonw18wd0vi93+LIC7/9uQNo/G2jxvZhHgAFAK3Dq07dB2oz3feIS++1s7Y9/AIP0D0cvWrj6aOnvZ39rFzoZOttd3sH5XC/Xt0RNVl03LYPGJ+VSdVEiB1tEROW7XLy/nUO/Am58oDn+qeGJzHZ09A3T29r85DJWZFqatq4+2rj7aRxjCguhQVE56hFlF2ZTmZVCSG30zyE6PDmtlREJkpIXeuh4JkRYJkRYKEQkbaWEj8ub1EJFQ9DItHNsWCmEhOPy2YmYYYAaGcfiDyZuXsW02vG0An2DiDf14hndmAnuG3K4FVozWxt37zawVKI5tf2HYY2fG8ZxH7bXag3zwuy/QPzhI38DYU95CBuVF2Zw9r5iqkwo5t7KEF2qaJ6I0kZT14xf3jLj9/PlHXpF2YNDp6Rugszf6iaG9u4+O2FBWR3c/+VlpNHb0UF3XTmNnb0LPchrxTQF7851l6LYrTj2Br/zxsgmtJ57QH+kta3iqjtYmnsdiZjcBN8VudpjZ1jjqOm47gd/F37wEaJyoWpKcXpvR6bUZnV6bYbYAd3zwzZtH+/qcFE+jeEK/FigfcnsWsG+UNrWx4Z18oDnOx+LudwJ3xlNwUMxsXTwfnVKRXpvR6bUZnV6bI5uo1yee+YdrgflmNtfM0oGVwKphbVYBN8SuXwus9uiXBauAlWaWYWZzgfnAi+NTuoiIHK0xe/qxMfpbgEeJTtm82903mtltwDp3XwXcBdxrZtVEe/grY4/daGYPAJuAfuATR5q5IyIiE2vM2TsSZWY3xYahZBi9NqPTazM6vTZHNlGvj0JfRCSFaE0BEZEUotAfxszKzexJM9tsZhvN7C9j24vM7HEz2x67LAy61qCYWdjMXjazh2K355rZmthrc3/sC/+UZGYFZvagmW2J7UNna9+JMrO/jv2fet3Mfmxmmam675jZ3WZWb2avD9k24n5iUV83s2oze83MTj+e51bov10/8P/c/RTgLOATseUkbgWecPf5wBOx26nqL4HNQ27fDtwRe21aiK61lKq+BvzG3U8G3kH0dUr5fcfMZgKfAqrcfQnRSSErSd195wfA5cO2jbafXEF05uN8osczffu4ntnd9XOEH+CXRNcd2grMiG2bAWwNuraAXo9ZsR3yYuAhogfgNQKR2P1nA48GXWdAr800osf82bDtKb/v8NZR+0VEZw0+BFyWyvsOMAd4faz9BPgu0fXO3tbuWH7U0z8CM5sDnAasAcrcfT9A7HJ6cJUF6qvA3wKHj3svBg66++HFUiZsqY0kUAE0AP8dG/76vpnloH0Hd98L/CewG9gPtALr0b4z1Gj7yUhL4Rzz66TQH4WZ5QI/Bf7K3duCricRmNn7gHp3Xz908whNU3VKWAQ4Hfi2u58GdJKCQzkjiY1PXwXMJbribg7RYYvhUnXfOZJx/T+m0B+BmaURDfz/dfefxTbXmdmM2P0zgPqg6gvQucCVZvYGcB/RIZ6vAgWx5TdglKU2UkQtUOvua2K3HyT6JqB9B94F7HT3BnfvA34GnIP2naFG20/iWs4mXgr9YSy6JupdwGZ3/8qQu4YuNXED0bH+lOLun3X3We4+h+iXcKvd/cPAk0SX34AUfW0A3P0AsMfMFsY2XUL0aPSU33eIDuucZWbZsf9jh18b7TtvGW0/WQV8JDaL5yyg9fAw0LHQwVnDmNl5wO+BDbw1bv33RMf1HwBmE92Br3P3lF2L2cwuBD7j7u8zswqiPf8i4GXg/7h7T5D1BcXMlgHfB9KBGuCjRDtXKb/vmNkXgQ8SnSH3MvBnRMemU27fMbMfAxcSXUmzDvhH4BeMsJ/E3iS/SXS2zyHgo+5+zCcdUeiLiKQQDe+IiKQQhb6ISApR6IuIpBCFvohIClHoi4ikEIW+iEgKUeiLiKQQhb7IEGb2CzNbH1v3/abYthvNbJuZPWVm3zOzb8a2l5rZT81sbezn3GCrFxmbDs4SGcLMimJHQWYBa4ku//ss0TV02oHVwKvufouZ/Qj4L3d/xsxmE10W+JTAiheJQ2TsJiIp5VNmdnXsejnwJ8DTh5dNMLOfAAti978LWBQ9Sh6AaWaW5+7tk1mwyNFQ6IvExNYTehdwtrsfMrOniJ6wYrTeeyjWtmtyKhQ5fhrTF3lLPtASC/yTiZ4uMxu4wMwKY0sAXzOk/WPALYdvxBZbE0loCn2Rt/wGiJjZa8A/AS8Ae4F/JbrK6m+JLgfcGmv/KaAqdrLqTcDNk1+yyNHRF7kiYzCzXHfviPX0fw7c7e4/D7oukWOhnr7I2L5gZq8ArxM98fkvAq5H5Jippy8ikkLU0xcRSSEKfRGRFKLQFxFJIQp9EZEUotAXEUkhCn0RkRTy/wEQ4VcHRwai7AAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sn.distplot(train[\"age\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1eecc508748>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "train['job'].value_counts().plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1eecc5ca1d0>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "train['default'].value_counts().plot.bar()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "More than 90% of the clients have no default history. Now we will explore these variables against the target variable using bivariate analysis. We will make use of scatter plots for continuous or numeric variables and crosstabs for the categorical variables. Let's start with job and subscribed variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bivariate Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "subscribed       no  yes\n",
      "job                     \n",
      "admin.         3179  452\n",
      "blue-collar    6353  489\n",
      "entrepreneur    923   85\n",
      "housemaid       795   79\n",
      "management     5716  923\n",
      "retired        1212  362\n",
      "self-employed   983  140\n",
      "services       2649  254\n",
      "student         453  182\n",
      "technician     4713  594\n",
      "unemployed      776  129\n",
      "unknown         180   26\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Percentage')"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfUAAAIgCAYAAACcU/AQAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvnQurowAAIABJREFUeJzt3XmYXGWZ9/HvTVgSdoWgQsBEZJXdsCkiCAoIggsjoOKGoOMCrq8LLoiDyyAzOuqoqCDgAijDAIKAGyAqS8IaQQYElIgKIiJbgJD7/eOcSiqd7qQauuo5Of39XFeu9Kk6XXXTdOp3zrNGZiJJkpZ+y5QuQJIkjQ1DXZKkljDUJUlqCUNdkqSWMNQlSWoJQ12SpJYw1CVJaglDXZKkljDUJUlqiWVLFzBaa665Zk6dOrV0GZIkDcTMmTP/lpmTezl3qQv1qVOnMmPGjNJlSJI0EBHxh17PtfldkqSWMNQlSWoJQ12SpJZY6vrUJUnt99hjjzF79mzmzJlTupSBmThxIlOmTGG55ZZ7wq9hqEuSGmf27NmsssoqTJ06lYgoXU7fZSb33HMPs2fPZtq0aU/4dWx+lyQ1zpw5c1hjjTXGRaADRARrrLHGk26ZMNQlSY00XgK9Yyz+ew11SZJawlCXJLXOUUcdxec///kxfc0ZM2Zw+OGHj8nr96M+cKCcJElLNHfuXKZPn8706dNLl7JY3qlLkpYKDz74IHvvvTdbbrklm222GaeddhpTp07lb3/7G1DdSe+yyy7zz7/22mt50YtexAYbbMA3vvENAP785z+z8847s9VWW7HZZpvxy1/+EoDzzz+fbbbZhi233JLddtsNqO6mDzvsMF7ykpfw+te/nosuuoh99tlnsa8PcOyxx7LtttuyxRZb8IlPfGL+48cccwwbbbQRu+++OzfddFNffkbeqUuSlgrnn38+a6+9Nueeey4A9913Hx/84AdHPP+6667jsssu48EHH2Trrbdm77335vvf/z577LEHRx55JI8//jgPPfQQd999N4ceeiiXXHIJ06ZN4+9///v815g5cyaXXnopkyZN4qKLLlri68+aNYubb76ZK664gsxk33335ZJLLmGllVbi1FNP5eqrr2bu3Llss802PPe5zx3zn5GhLklaKmy++ea8//3v54Mf/CD77LMPL3jBCxZ7/n777cekSZOYNGkSu+66K1dccQXbbrstb37zm3nsscd4+ctfzlZbbcVFF13EzjvvPH9++FOf+tT5r7HvvvsyadKknl//0ksv5cILL2TrrbcG4IEHHuDmm2/m/vvv5xWveAUrrrji/NftB5vfJUlLhQ033JCZM2ey+eab8+EPf5ijjz6aZZddlnnz5gEsMsd76BSxiGDnnXfmkksuYZ111uHggw/m5JNPJjNHnE620korjVjPcK+fmXz4wx/mmmuu4ZprruGWW27hkEMOGfb8fjDUJUlLhTvvvJMVV1yR173udbz//e/nqquuYurUqcycOROAM844Y6HzzzrrLObMmcM999zDRRddxLbbbssf/vAH1lprLQ499FAOOeQQrrrqKnbccUcuvvhibrvtNoCFmt8XZ7jX32OPPTjhhBN44IEHAPjTn/7EXXfdxc4778yZZ57Jww8/zP33388555wzhj+ZBfrW/B4RJwD7AHdl5mbDPB/AF4GXAg8Bb8zMq/pVjyRp6Xb99dfzgQ98gGWWWYbllluOr371qzz88MMccsghfPrTn2b77bdf6PztttuOvffemz/+8Y987GMfY+211+akk07i2GOPZbnllmPllVfm5JNPZvLkyRx//PG88pWvZN68eay11lr85Cc/WWI9w73+2muvzY033siOO+4IwMorr8x3vvMdttlmGw444AC22mornvnMZy6x6+CJiszszwtH7Aw8AJw8Qqi/FHgXVahvD3wxM7cfet5Q06dPzxkzZox1uZKkBrnxxhvZZJNNSpcxcMP9d0fEzMzsaS5d35rfM/MSYHFtGPtRBX5m5mXA6hHxjH7VI0lS25XsU18HuKPreHb9mCRJegJKTmkbbhjgsH0BEXEYcBjAeuutt+RXPmq1J1PXkNe6bwxfa4zqsqZRvNYY1WVNo3itFv9ONbEmaPfv1J1Xj83rAKy99di91ljVNZY1UfZOfTawbtfxFODO4U7MzOMzc3pmTp88efJAipMkaWlTMtTPBl4flR2A+zLzzwXrkSRpqdbPKW3fB3YB1oyI2cAngOUAMvNrwHlUI99voZrS9qZ+1SJJ0njQt1DPzIOW8HwC7+jX+0uS2m3qfw3bY7sYiz//9s/u/cSLaQhXlJMkqSUMdUmSenT77bezySabcOgHPsVzdt2flxz0dh5+eA7XzLqJHfZ5PVvs/mpeccj7uPcf/yxSn6EuSdIo3HzzzbzjDa/mt7/4IauvugpnnPczXv/uj/G5I4/gup+ezuYbP5tP/sfXi9RmqEuSNArTpk1jq802AuC5W2zC7/8wm3/c9wAv3LHaH/0N/7IPl1w+hvPrR8FQlyRpFFZYYYX5X0+YsAz/uO/+gtUszFCXJOlJWG3VlXnKaqvwy8urjUZPOeNcXrjDNkVqKblMrCRJT9jth689um8Y4yVZu530haN524eO4aE5c3jWelM48T+O6tt7LY6hLklSj6ZOncqsWbPmr/3+/re9fv5zl/3o5FJlzWfzuyRJLWGoS5LUEoa6JEktYahLktQShrokSS1hqEuS1BJOaZMkLZ2O32VsX++o+8b29QrwTl2SpJbwTl2SpB587GMfY8011+SII44A4MjPfpmnTV6DRx59lNPP+QmPPPoor9hzVz75/n/lwYce5tVv/SCz//xXHp83j48d8RYO2G+PvtfonbokST045JBDOOmkkwCYN28ep559IU9b86ncfNsfueLcU7jmwlOZed2NXHLZTM7/xa9Z++mTufanpzHr5z9gz12fN5AaDXVJknowdepU1lhjDa6++mouvPg3bP2cjbjy2hu48OLL2PolB7HNHq/hd7+/nZtvu4PNN342P/3l5XzwmC/yy8uvYrVVVxlIjTa/S5LUo7e85S18+9vf5i+33cibD9yPn116BR9+55t468H7L3LuzB9/l/N+fikf/syXeckLd+Dj7zms7/V5py5JUo9e8YpXcP7553PltTewxy47sscuO3LCaWfzwIMPAfCnP9/FXX/7O3f+5W5WnDSR171qb97/toO56vrfDaQ+79QlSUunwy4a3fljsPXq8ssvz6677srqyz7ChAkTeMkLd+TGm29jx33fCMDKK07iO1/6N265/Q4+8G9fYJlYhuWWW5avfuYjT/q9e2GoS5LUo3nz5nHZZZfxgy9/cv5jR7zlNRzxltcsdN76U9dlj10GMzium83vkiT14IYbbuDZz342u+22Gxs8a73S5QzLO/UBmjrne2PyOrePyatIkkZj00035dZbb60O7ry6bDEj8E5dktRImVm6hIEai/9eQ12S1DgTJ07knnvuGTfBnpncc889TJw48Um9js3vkqTGmTJlCrNnz+buv9wFxNi86H03js3rAPzjrrF5na6aJk6cyJQpU57Uyxnq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\n",
      "text/plain": [
       "<Figure size 576x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(pd.crosstab(train['job'],train['subscribed']))\n",
    "\n",
    "job=pd.crosstab(train['job'],train['subscribed'])\n",
    "job.div(job.sum(1).astype(float), axis=0).plot(kind=\"bar\", stacked=True, figsize=(8,8))\n",
    "plt.xlabel('Job')\n",
    "plt.ylabel('Percentage')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the above graph we can infer that students and retired people have higher chances of subscribing to a term deposit, which is surprising as students generally do not subscribe to a term deposit. The possible reason is that the number of students in the dataset is less and comparatively to other job types, more students have subscribed to a term deposit.\n",
    "\n",
    "Next, let's explore the default variable against the subscribed variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "subscribed     no   yes\n",
      "default                \n",
      "no          27388  3674\n",
      "yes           544    41\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Percentage')"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Rl2SpEIYdUmSCmHUJUkqhFGXJKkQRl2SpEL0bfYAkhq3evVq2traWLVqVbNH6Tb9+/dn6NCh9OvXr9mjSNs8oy71IG1tbey88860tLQQEc0ep3KZyfLly2lra2PYsGHNHkfa5nn4XepBVq1axR577NErgg4QEeyxxx696siEtCWMutTD9Jagr9Pbfl9pSxh1qRe57LLL+P73v79Vtzl37lzOO++8rbL9KuaTehPPqUvabGvWrKG1tZXW1tZmjyIJ99SlHu+tt97ixBNP5JBDDuGggw7iZz/7GS0tLbz00ktAbU/6qKOOWr/+Y489xqc//WmGDx/OtddeC8Cf/vQnxo4dy6hRozjooIOYNWsWAPfeey9jxozhkEMO4ZhjjgFqe9OTJ09m3LhxnHXWWcyYMYOTTjppo9sHuPLKKznssMM4+OCDufTSS9c//+1vf5sDDjiAY489lqeeeqqyf09Sb+CeutTD3XvvvQwZMoRf/epXALz22mtcdNFFG1x/wYIFzJ49m7feeovRo0dz4okncuutt3LcccdxySWX8O6777JixQqWLVvGpEmTmDlzJsOGDePll19ev4158+bx0EMPMWDAAGbMmLHJ7S9cuJAlS5YwZ84cMpPx48czc+ZMdtppJ2677TYeffRR1qxZw5gxYzj00EMr+fck9QZGXerhRo4cyQUXXMBFF13ESSedxCc/+cmNrn/yySczYMAABgwYwNFHH82cOXM47LDDOOecc1i9ejWnnHIKo0aNYsaMGYwdO3b9W8l233339dsYP348AwYMaHj7Dz30EPfffz+jR48G4M0332TJkiW88cYbTJgwgR133HH9diVtPg+/Sz3chz70IebNm8fIkSOZMmUKV1xxBX379mXt2rUAf/F2sI5Xk0cEY8eOZebMmey999584Qtf4MYbbyQzN3jl+U477bTBeTrbfmYyZcoU5s+fz/z581m6dCkTJ07sdH1Jm8+oSz3cCy+8wI477siZZ57JBRdcwCOPPEJLSwvz5s0D4M4773zP+nfddRerVq1i+fLlzJgxg8MOO4w//OEP7LnnnkyaNImJEyfyyCOPcOSRR/Lb3/6WZ555BuA9h983prPtH3fccVx33XW8+eabADz//PO8+OKLjB07ll/84hesXLmSN954g3vuuWcr/puReh8Pv0s93OOPP86FF17IdtttR79+/bj6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\n",
      "text/plain": [
       "<Figure size 576x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(pd.crosstab(train['default'],train['subscribed']))\n",
    "\n",
    "default=pd.crosstab(train['default'],train['subscribed'])\n",
    "default.div(default.sum(1).astype(float), axis=0).plot(kind=\"bar\", stacked=True, figsize=(8,8))\n",
    "plt.xlabel('default')\n",
    "plt.ylabel('Percentage')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can infer that clients having no previous default have slightly higher chances of subscribing to a term loan as compared to the clients who have previous default history.\n",
    "\n",
    "Let's now look at how correlated our numerical variables are. We will see the correlation between each of these variables and the variable which have high negative or positive values are correlated. By this we can get an overview of the variables which might affect our target variable. We will convert our target variable into numeric values first."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "train['subscribed'].replace('no', 0,inplace=True)\n",
    "train['subscribed'].replace('yes', 1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1eecc766208>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "corr = train.corr()\n",
    "mask = np.array(corr)\n",
    "mask[np.tril_indices_from(mask)] = False\n",
    "fig,ax= plt.subplots()\n",
    "fig.set_size_inches(20,10)\n",
    "sn.heatmap(corr, mask=mask,vmax=.9, square=True,annot=True, cmap=\"YlGnBu\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can infer that duration of the call is highly correlated with the target variable. This can be verified as well. As the duration of the call is more, there are higher chances that the client is showing interest in the term deposit and hence there are higher chances that the client will subscribe to term deposit.\n",
    "\n",
    "Next we will look for any missing values in the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ID            0\n",
       "age           0\n",
       "job           0\n",
       "marital       0\n",
       "education     0\n",
       "default       0\n",
       "balance       0\n",
       "housing       0\n",
       "loan          0\n",
       "contact       0\n",
       "day           0\n",
       "month         0\n",
       "duration      0\n",
       "campaign      0\n",
       "pdays         0\n",
       "previous      0\n",
       "poutcome      0\n",
       "subscribed    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are no missing values in the train dataset. \n",
    "\n",
    "Next, we will start to build our predictive model to predict whether a client will subscribe to a term deposit or not.\n",
    "\n",
    "As the sklearn models takes only numerical input, we will convert the categorical variables into numerical values using dummies. We will remove the ID variables as they are unique values and then apply dummies. We will also remove the target variable and keep it in a separate variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Model Building"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "target = train['subscribed']\n",
    "train = train.drop('subscribed',1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# applying dummies on the train dataset\n",
    "train = pd.get_dummies(train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, its time to build our model. We will split the train data into training and validation set so that we will be able to validate the results of our model on the validation set. We will keep 20% data as validation set and rest as the training set. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# splitting into train and validation with 20% data in validation set and 80% data in train set.\n",
    "X_train, X_val, y_train, y_val = train_test_split(train, target, test_size = 0.2, random_state=12)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now our data is ready. Its time to build our model and check its performance. Logistic regression is used for classification problems and as it is a classification problem let's first build a Logistic Regression model."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "# defining the logistic regression model\n",
    "lreg = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
       "          n_jobs=None, penalty='l2', random_state=None, solver='warn',\n",
       "          tol=0.0001, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# fitting the model on  X_train and y_train\n",
    "lreg.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "# making prediction on the validation set\n",
    "prediction = lreg.predict(X_val)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we will evaluate how accurate our predictions are. As the evaluation metric for this problem is accuracy, let's calculate the accuracy on validation set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9048973143759874"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# calculating the accuracy score\n",
    "accuracy_score(y_val, prediction)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We got an accuracy score of around 90% on the validation dataset. Logistic regression has a linear decision boundary. What if our data have non linearity? We need a model that can capture this non linearity. \n",
    "\n",
    "Let's try decision tree algorithm now to check if we get better accuracy with that. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Decision Tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# defining the decision tree model with depth of 4, you can tune it further to improve the accuracy score\n",
    "clf = DecisionTreeClassifier(max_depth=4, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=4,\n",
       "            max_features=None, max_leaf_nodes=None,\n",
       "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "            min_samples_leaf=1, min_samples_split=2,\n",
       "            min_weight_fraction_leaf=0.0, presort=False, random_state=0,\n",
       "            splitter='best')"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# fitting the decision tree model\n",
    "clf.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "# making prediction on the validation set\n",
    "predict = clf.predict(X_val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9042654028436019"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# calculating the accuracy score\n",
    "accuracy_score(y_val, predict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We got an accuracy of more than 90% on the validation set. You can try to improve the score by tuning hyperparameters of the model. Let's now make the prediction on test dataset. We will make the similar changes in the test set as we have done in the training set before making the predictions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "test = pd.get_dummies(test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "test_prediction = clf.predict(test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, we will save these predictions into a csv file. You can then open this csv file and copy paste the predictions on the provided excel file to generate score."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "submission = pd.DataFrame()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating a Business_Sourced column and saving the predictions in it\n",
    "submission['ID'] = test['ID']\n",
    "submission['subscribed'] = test_prediction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since the target variable is yes or no, we will convert 1 and 0 in the predictions to yes and no respectively."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "submission['subscribed'].replace(0,'no',inplace=True)\n",
    "submission['subscribed'].replace(1,'yes',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "submission.to_csv('submission.csv', header=True, index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now you have the submission file with you. Follow these steps to generate your score:\n",
    "1. Open the submission.csv file.\n",
    "2. Copy the values in the subscribed column and paste them in the subscribed column of solution_checker.xlsx file.\n",
    "3. You will see the accuracy of the model on test dataset under Your accuracy score column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r'C:\\Users\\BASUKI NANDAN TIWARI\\Documents\\submission.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>subscribed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>38441</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>40403</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3709</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>37422</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>12527</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>16013</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>196</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8516</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>31208</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>38462</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>17041</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>4920</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>802</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>1738</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>9565</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>29743</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>34946</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>1671</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>2868</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>6478</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>1572</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>44771</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>30088</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>19021</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>15704</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>39812</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>21170</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>923</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>17887</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>6778</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>470</th>\n",
       "      <td>7876</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>471</th>\n",
       "      <td>22489</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>472</th>\n",
       "      <td>25370</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>473</th>\n",
       "      <td>5305</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>474</th>\n",
       "      <td>28263</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>475</th>\n",
       "      <td>42316</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>476</th>\n",
       "      <td>16756</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>477</th>\n",
       "      <td>7726</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>478</th>\n",
       "      <td>43968</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>479</th>\n",
       "      <td>33522</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>480</th>\n",
       "      <td>12060</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>481</th>\n",
       "      <td>25476</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>482</th>\n",
       "      <td>44314</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>483</th>\n",
       "      <td>29020</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>484</th>\n",
       "      <td>2017</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>485</th>\n",
       "      <td>24187</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>486</th>\n",
       "      <td>27980</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>487</th>\n",
       "      <td>9229</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>488</th>\n",
       "      <td>32738</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>489</th>\n",
       "      <td>15465</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>490</th>\n",
       "      <td>23820</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>491</th>\n",
       "      <td>20667</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>492</th>\n",
       "      <td>35462</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>493</th>\n",
       "      <td>2888</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>494</th>\n",
       "      <td>10283</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>495</th>\n",
       "      <td>4406</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>496</th>\n",
       "      <td>11259</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>497</th>\n",
       "      <td>4430</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>498</th>\n",
       "      <td>31356</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>499</th>\n",
       "      <td>37769</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>500 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        ID subscribed\n",
       "0    38441         no\n",
       "1    40403        yes\n",
       "2     3709         no\n",
       "3    37422         no\n",
       "4    12527         no\n",
       "5    16013         no\n",
       "6      196         no\n",
       "7     8516         no\n",
       "8    31208        yes\n",
       "9    38462         no\n",
       "10   17041         no\n",
       "11    4920         no\n",
       "12     802         no\n",
       "13    1738         no\n",
       "14    9565         no\n",
       "15   29743        yes\n",
       "16   34946         no\n",
       "17    1671         no\n",
       "18    2868         no\n",
       "19    6478         no\n",
       "20    1572         no\n",
       "21   44771        yes\n",
       "22   30088         no\n",
       "23   19021         no\n",
       "24   15704        yes\n",
       "25   39812        yes\n",
       "26   21170         no\n",
       "27     923         no\n",
       "28   17887         no\n",
       "29    6778         no\n",
       "..     ...        ...\n",
       "470   7876         no\n",
       "471  22489         no\n",
       "472  25370         no\n",
       "473   5305         no\n",
       "474  28263         no\n",
       "475  42316        yes\n",
       "476  16756         no\n",
       "477   7726         no\n",
       "478  43968        yes\n",
       "479  33522         no\n",
       "480  12060         no\n",
       "481  25476         no\n",
       "482  44314        yes\n",
       "483  29020         no\n",
       "484   2017         no\n",
       "485  24187         no\n",
       "486  27980         no\n",
       "487   9229         no\n",
       "488  32738         no\n",
       "489  15465        yes\n",
       "490  23820         no\n",
       "491  20667         no\n",
       "492  35462        yes\n",
       "493   2888         no\n",
       "494  10283         no\n",
       "495   4406         no\n",
       "496  11259         no\n",
       "497   4430         no\n",
       "498  31356        yes\n",
       "499  37769         no\n",
       "\n",
       "[500 rows x 2 columns]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(13564, 2)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
