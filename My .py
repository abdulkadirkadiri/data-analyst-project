{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "# Project: Medical Appointment Analysis \n",
    "\n",
    "## Table of Contents\n",
    "<ul>\n",
    "<li><a href=\"#intro\">Introduction</a></li>\n",
    "<li><a href=\"#wrangling\">Data Wrangling</a></li>\n",
    "<li><a href=\"#eda\">Exploratory Data Analysis</a></li>\n",
    "<li><a href=\"#conclusions\">Conclusions</a></li>\n",
    "</ul>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='intro'></a>\n",
    "## Introduction\n",
    "This dataset is  used  to investigate and analyze the factors that are important to predict if  a patient will show up for their scheduled appointment.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='wrangling'></a>\n",
    "## Data Wrangling\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "# Load your data \n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "% matplotlib inline\n",
    "df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv' )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>PatientId</th>\n",
       "      <th>AppointmentID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>ScheduledDay</th>\n",
       "      <th>AppointmentDay</th>\n",
       "      <th>Age</th>\n",
       "      <th>Neighbourhood</th>\n",
       "      <th>Scholarship</th>\n",
       "      <th>Hipertension</th>\n",
       "      <th>Diabetes</th>\n",
       "      <th>Alcoholism</th>\n",
       "      <th>Handcap</th>\n",
       "      <th>SMS_received</th>\n",
       "      <th>No-show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.987250e+13</td>\n",
       "      <td>5642903</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T18:38:08Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>62</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.589978e+14</td>\n",
       "      <td>5642503</td>\n",
       "      <td>M</td>\n",
       "      <td>2016-04-29T16:08:27Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.262962e+12</td>\n",
       "      <td>5642549</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T16:19:04Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>62</td>\n",
       "      <td>MATA DA PRAIA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.679512e+11</td>\n",
       "      <td>5642828</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T17:29:31Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>8</td>\n",
       "      <td>PONTAL DE CAMBURI</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8.841186e+12</td>\n",
       "      <td>5642494</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T16:07:23Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      PatientId  AppointmentID Gender          ScheduledDay  \\\n",
       "0  2.987250e+13        5642903      F  2016-04-29T18:38:08Z   \n",
       "1  5.589978e+14        5642503      M  2016-04-29T16:08:27Z   \n",
       "2  4.262962e+12        5642549      F  2016-04-29T16:19:04Z   \n",
       "3  8.679512e+11        5642828      F  2016-04-29T17:29:31Z   \n",
       "4  8.841186e+12        5642494      F  2016-04-29T16:07:23Z   \n",
       "\n",
       "         AppointmentDay  Age      Neighbourhood  Scholarship  Hipertension  \\\n",
       "0  2016-04-29T00:00:00Z   62    JARDIM DA PENHA            0             1   \n",
       "1  2016-04-29T00:00:00Z   56    JARDIM DA PENHA            0             0   \n",
       "2  2016-04-29T00:00:00Z   62      MATA DA PRAIA            0             0   \n",
       "3  2016-04-29T00:00:00Z    8  PONTAL DE CAMBURI            0             0   \n",
       "4  2016-04-29T00:00:00Z   56    JARDIM DA PENHA            0             1   \n",
       "\n",
       "   Diabetes  Alcoholism  Handcap  SMS_received No-show  \n",
       "0         0           0        0             0      No  \n",
       "1         0           0        0             0      No  \n",
       "2         0           0        0             0      No  \n",
       "3         0           0        0             0      No  \n",
       "4         1           0        0             0      No  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking the dataset\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(110527, 14)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking dimension\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 110527 entries, 0 to 110526\n",
      "Data columns (total 14 columns):\n",
      "PatientId         110527 non-null float64\n",
      "AppointmentID     110527 non-null int64\n",
      "Gender            110527 non-null object\n",
      "ScheduledDay      110527 non-null object\n",
      "AppointmentDay    110527 non-null object\n",
      "Age               110527 non-null int64\n",
      "Neighbourhood     110527 non-null object\n",
      "Scholarship       110527 non-null int64\n",
      "Hipertension      110527 non-null int64\n",
      "Diabetes          110527 non-null int64\n",
      "Alcoholism        110527 non-null int64\n",
      "Handcap           110527 non-null int64\n",
      "SMS_received      110527 non-null int64\n",
      "No-show           110527 non-null object\n",
      "dtypes: float64(1), int64(8), object(5)\n",
      "memory usage: 11.8+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
       "      <th>PatientId</th>\n",
       "      <th>AppointmentID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Scholarship</th>\n",
       "      <th>Hipertension</th>\n",
       "      <th>Diabetes</th>\n",
       "      <th>Alcoholism</th>\n",
       "      <th>Handcap</th>\n",
       "      <th>SMS_received</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1.105270e+05</td>\n",
       "      <td>1.105270e+05</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.474963e+14</td>\n",
       "      <td>5.675305e+06</td>\n",
       "      <td>37.088874</td>\n",
       "      <td>0.098266</td>\n",
       "      <td>0.197246</td>\n",
       "      <td>0.071865</td>\n",
       "      <td>0.030400</td>\n",
       "      <td>0.022248</td>\n",
       "      <td>0.321026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.560949e+14</td>\n",
       "      <td>7.129575e+04</td>\n",
       "      <td>23.110205</td>\n",
       "      <td>0.297675</td>\n",
       "      <td>0.397921</td>\n",
       "      <td>0.258265</td>\n",
       "      <td>0.171686</td>\n",
       "      <td>0.161543</td>\n",
       "      <td>0.466873</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>3.921784e+04</td>\n",
       "      <td>5.030230e+06</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.172614e+12</td>\n",
       "      <td>5.640286e+06</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.173184e+13</td>\n",
       "      <td>5.680573e+06</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>9.439172e+13</td>\n",
       "      <td>5.725524e+06</td>\n",
       "      <td>55.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.999816e+14</td>\n",
       "      <td>5.790484e+06</td>\n",
       "      <td>115.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          PatientId  AppointmentID            Age    Scholarship  \\\n",
       "count  1.105270e+05   1.105270e+05  110527.000000  110527.000000   \n",
       "mean   1.474963e+14   5.675305e+06      37.088874       0.098266   \n",
       "std    2.560949e+14   7.129575e+04      23.110205       0.297675   \n",
       "min    3.921784e+04   5.030230e+06      -1.000000       0.000000   \n",
       "25%    4.172614e+12   5.640286e+06      18.000000       0.000000   \n",
       "50%    3.173184e+13   5.680573e+06      37.000000       0.000000   \n",
       "75%    9.439172e+13   5.725524e+06      55.000000       0.000000   \n",
       "max    9.999816e+14   5.790484e+06     115.000000       1.000000   \n",
       "\n",
       "        Hipertension       Diabetes     Alcoholism        Handcap  \\\n",
       "count  110527.000000  110527.000000  110527.000000  110527.000000   \n",
       "mean        0.197246       0.071865       0.030400       0.022248   \n",
       "std         0.397921       0.258265       0.171686       0.161543   \n",
       "min         0.000000       0.000000       0.000000       0.000000   \n",
       "25%         0.000000       0.000000       0.000000       0.000000   \n",
       "50%         0.000000       0.000000       0.000000       0.000000   \n",
       "75%         0.000000       0.000000       0.000000       0.000000   \n",
       "max         1.000000       1.000000       1.000000       4.000000   \n",
       "\n",
       "        SMS_received  \n",
       "count  110527.000000  \n",
       "mean        0.321026  \n",
       "std         0.466873  \n",
       "min         0.000000  \n",
       "25%         0.000000  \n",
       "50%         0.000000  \n",
       "75%         1.000000  \n",
       "max         1.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Summary  statistics \n",
    "df.describe()"
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
       "0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#null values in the columns\n",
    "df.isnull().sum().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='eda'></a>\n",
    "## Exploratory Data Analysis\n",
    "\n",
    "\n",
    "### Research Question (factors that are important to predict if a patient will show up)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#drop columns\n",
    "df.drop(['PatientId','AppointmentID','Neighbourhood'], axis=1, inplace= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# rename some columns\n",
    "df.rename(columns = {'Gender':'gender','ScheduledDay':'schedule','Age':'age','Neighbourhood':'neighbourhood','Scholarship':'scholarship','Hipertension':'hypertension' ,'Diabetes':'diabetes' ,'Alcoholism':'alcohol','Handcap':'handicap','SMS_received':'sms_received', \n",
    "                     'No-show':'No_show'},inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
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
       "      <th>gender</th>\n",
       "      <th>schedule</th>\n",
       "      <th>AppointmentDay</th>\n",
       "      <th>age</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcohol</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>No_show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T18:38:08Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>2016-04-29T16:08:27Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>56</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T16:19:04Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T17:29:31Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>8</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T16:07:23Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>56</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender              schedule        AppointmentDay  age  scholarship  \\\n",
       "0      F  2016-04-29T18:38:08Z  2016-04-29T00:00:00Z   62            0   \n",
       "1      M  2016-04-29T16:08:27Z  2016-04-29T00:00:00Z   56            0   \n",
       "2      F  2016-04-29T16:19:04Z  2016-04-29T00:00:00Z   62            0   \n",
       "3      F  2016-04-29T17:29:31Z  2016-04-29T00:00:00Z    8            0   \n",
       "4      F  2016-04-29T16:07:23Z  2016-04-29T00:00:00Z   56            0   \n",
       "\n",
       "   hypertension  diabetes  alcohol  handicap  sms_received  No_show  \n",
       "0             1         0        0         0             0        0  \n",
       "1             0         0        0         0             0        0  \n",
       "2             0         0        0         0             0        0  \n",
       "3             0         0        0         0             0        0  \n",
       "4             1         1        0         0             0        0  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#replace the no_show columns\n",
    "df['No_show'].replace(('Yes', 'No'), (1, 0), inplace=True)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# creat mask\n",
    "No_show =  df.No_show == True\n",
    "did_show = df.No_show == False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZoAAAEqCAYAAAAszJYWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzt3Xm4HEW9//H3hyQQQJYQAgJh1YhEJCzRIEgEoxAWL1wFZZFERKNeZBFUUO4PIojgvSoSFxRlCYtAQJawGXNZA7IkQXZUwpoQhGyEEPbw/f1RdaBzmDlnJpk+y5zP63nOc2aqq2uqa7r7211d062IwMzMrCwrdHYFzMysuTnQmJlZqRxozMysVA40ZmZWKgcaMzMrlQONmZmVyoGmHZJ+KOmPnV2PFpKekvSZzvi89tqio+tWC0m3SPpaZ9ejTJI2kvSypF5t5AlJH+zIenVlkn4saa6kf9eYf6ykC5fxs7rUPqRI0lck3V725zRloMk7vFfzxve8pHMlva+G+XaWNKuYFhE/iYjl3lFJ2iRv7L3rmOc8ST9e3s8ulLdcO91GtUW9ekKwWB4R8UxEvC8ilkDzt1el7bTO+TcEjgEGR8T7G11+a5213XQlTRloss9FxPuAbYGPAf/dyfUx65bqOTjqJjYG5kXEC51dke7ctm2dQb9HRDTdH/AU8JnC+/8Frs2vDwEeBRYBTwDfyOmrAq8CbwMv57/1gbHAhYWytgf+BrwI3A/sXJh2C3AycEcu/6/A2nnaM0AUyv5EO8swBngTeCPnv6awbN8FHgAWApcCffO0fsC1wBxgQX49ME87BVgCvJbL+3WVzz0YeBqYBxxfbMsKbVE1b4VyzwN+A1yX2+Zu4AOF6TsAU/MyTQV2qLXeQF/gwlyPF/P867b3neTp/wE8nOe7BdiisJ5cU8g3A5hQeD8T2LpCXXYGZlVbH3MbXp6/t0XAvcCQKm32I+BX+XUfYDHwP/n9yrlN+gGbkNat3tXaK0//JvBYXjd+A6jK57bU8ULgJeBrpIPS44DHcztPANaqsf1PBe7J3+3VLfPVsD2tBZwLzM51vooq22mFZVgDOJ+0LTxNOtBcAfhMq/nPazVfW/uBCbnMRXmdGVqYb33gz/nzngSOaNWeF+bXLd/VoaR9wm1VvoPvA8/lZf9anueDedpKwM/y/M8DvwNWLq5/pDO2F3IZhxTK7Q9MzN/rPaRt4/bC9A8Dk4H5wD+BL7bahs8ErietixW39YrL08gdfFf5Y+kNe8O8Upyc3+8JfAAQ8CngFWDbNnYSxZVkA9LGtEdeaT+b3w8obFSPAx8i7QhuAU5rtYL1rmM5zgN+XGHZ7skr9lqkoPnNwkr0BWAVYDXgMuCqwry3AF9r4/MGkzas4Xll/gXwFhUCTXt5qyzLfODjpB3iRcAlhR3KAlLg6g0ckN/3r7He3wCuycvdC9gOWL2G7+RDeYP5LGlH/n1SQFkR2Iy081sBWI+0s3o2z7dZrt8KFepSaR16qlUbvgnsmz/zu6QdU58KZX0aeDC/3iEvx92FafdXWrcqtVeefi2wJrARaYc4skp7ttRxn7z8KwNHAXcBA/P3/Xvg4hrb/1lgS9JO/M/Uvj1dRwrI/XJbfapaG1dYhvNJQW213D7/Ag6tZf4q3+FYUvDeIy/jqcBdedoKwHTghMK68wSwW4XtpuW7Oj+3x8oVPn8k8G/gI7lNL2DpQPNLUrBYKy/fNcCphbq/BZyU22wP0j6uX55+CSlgrpq/k2fJgSanzSQdZPUm9QbNBT5S2IYXAjvmZe5b676smbvOrpL0InA7cCvwE4CIuC4iHo/kVtIR7k41lvll4PqIuD4i3o6IycA00pfZ4tyI+FdEvEr6Qrdu1AIVjIuI2RExn7SSbQ0QEfMi4s8R8UpELCId3X6qjnL3JZ353RYRrwP/j3Rkt7x5W1wREfdExFukQNPSNnsCj0XEBRHxVkRcDPwD+FyN9X6TFGQ/GBFLImJ6RLxUmF7tO/kScF1ETI6IN0lHiSuTzqaeIB25bk1qw0nAs5I+nN9PiYj2lrea6RFxef7MX5DOCLavkO9OYJCk/qSAfjawQb7e+CnSel2P0yLixYh4BriZttfNOyPiqryev0oKJsdHxKz8fY8F9s1dP+21/wUR8VBELCatJ1/M3S5VtydJ6wG7kw6iFkTEm3l7bVcu+0vADyJiUUQ8BfycdCCzPG7PdV1C2vkPyekfIwXHkyLijbzu/AHYv42yxkbE4ty2rX2RtM4+HBGvkM5sW5ZNwNeB70TE/Lyd/6TVZ70JnJTb7HrSAeHmuV2+AJyQP/shYHxhvr2ApyLi3Lwd3ks6MNi3kOfqiLgjf1+vtd1c7+q2/YM12Cci/q91oqTdgRNJR7MrkI4YHqyxzI2B/SQVd4B9SBtti+IolleAdgchLIPWn7E+gKRVgNNJR0T98vTVJPXKG0d71icd0QAQEYslzWtA3mr1bmmb9UlnDEVPk454a3EB6cz1Eklrkrpxjs878po/NyLeljSz8Lm3ko4QP5hfv0jawX+C+nfyRcV2eztfeF6/daaIeFXStPyZw0kHDluTjig/Bfyqzs+tZ92c2er9xsCVkorBdQmwLu23f7Gsp0nbzNq0vT1tCMyPiAW1LFgra5POLIrrVD3rUzWt269vDrQbA+vnA9sWvYApbZTVun2L1icF3Ep5B5D2WdNTzAFS70zxesm8fDBXrOv78ry9ee/30WJjYFir5ehN+n5rqXdVzXxG8x6SViJF6J+R+pDXJPU3tnxj0U4RM0lHZ2sW/laNiNNq+Pj2ym7EPMcAmwPDImJ10s4Jal++50gbeJopBa7+DcjbntmklbxoI9JpPbRT73zk9qOIGEzqYtoLGFXv5+ajxQ0Ln9sSaHbKr28l7eDbOptYTNoRtJTZi7SBFxXbbQVSd9TsKuXdSuom24Z07eNWYDdSF+RtVeZZlnWtvTJmAru3Wvf7RsSzNbT/hoXXG5GOuOfS9vY0E1grB656l29u/oziOlVcn9pTb/vNBJ5stRyrRcQebczT1mc8R1onWhTbby7pGtJHCp+1RqSBT+2ZQ+pWa/19FJfj1lbL8b6I+FaN9a6qRwUa0lHOSuQGz2c3uxamPw/0l7RGlfkvBD4naTdJvST1zUMhB1bJXzSH1LW0WR31fb7O/KuRVsIXJa1FOnOrp7zLgb0kfVLSiqR+3mrrSD1523M98CFJB0rqLelLpGtA19ZSb0m7SPpo3qm/RNrJ1HIGNwHYU9IISX1Igfp10sVpSDv1XUj96LNIR6gjSQH171XK/BfpSHfPXOZ/k9a5ou0kfT4fDR+VP/OuKuXdStppPxIRb5Cvv5B2bHOqzFPvelOL3wGnSNoYQNIASXvn1+21/5clDc4HIycBl+cz7KrbU0Q8B9wA/FZSP0l9JLUcOLW5neayJ+T6rpbrfHT+vFq0tx9o7R7gJUnHSlo5L8uWkj5W4/ytTQAOkbRFbrMTWibk7to/AKdLWgdA0gaSdmuv0NwuVwBjJa0iaTAwupDlWtJ2eHBu7z6SPiZpi2Vcjnf0qECT+zOPIH2RC4ADSRfVWqb/A7gYeELSi5LWbzX/TGBv4IekwDET+B41tGPuaz0FuCOXXalPvrWzgcE5/1U15P8l6RrDXNKO6y+tpp9B6ldfIGlchTo+DBwG/Il0VLWANIKl0vLUnLc9ETGPdBR8DOli8PeBvSJibi31Bt5PCnwvkQZH3EoNO5WI+CfpOsGvSG32OdKw+Dfy9H+R+ren5PcvkS7y3lGtKzIiFgL/BfyRdAS9mPe2y9WkawgtAyA+X+hmau1vpO+05ezlEdJF6WpnM9B+ey2LM0jbyl8lLSKtX8PytPba/wLSheR/k65HHQE1bU8Hk4LWP0gjqI7K87W5nWaHk9r+CdJ12j8B59SyoDWWX8y/hLTubE0a2DGX9P3XGqhal3cDMI7UhTiDdK0O0gEJwLE5/S5JLwH/R+rJqMW3Sd1o/yZ9J+cWPncR6cB7f9IZ9r+Bn/LeA6W6KaIRZ9lmVgtJY0kXzb/c2XXpCJJuIY246pK/jO8O8hnFQ8BKra69dBs96ozGzKw7kPSfklaU1I90VnFNdw0y4EBjZtYVfYPUnfg46XrXt9rO3rWV3nWWR438kfTjoAC+SvrF6aWkHy89Rfr16YI86ucM3v2R0VfyWG4kjebd28j8OCLG5/TtSH2NK5MuKh8Z7g80M+syOuKM5gzgLxHxYdIPnB4l3crixogYBNyY30P6gdag/DeGdLsDCiOohpGGdZ6YTynJecYU5hvZActkZmY1KvWMRtLqpPsXbVY8y5D0T9I9jZ7LvwC+JSI2l/T7/PriYr6Wv4j4Rk7/PWmY5y3AzTmIIemAYr5K1l577dhkk00avKRmZs1t+vTpcyOi9W/CalL2nQE2I/UznitpCOl+QEeSfiz5HEAONuvk/Buw9C9PZ+W0ttJnVUhfiqQxpLMeNtpoI6ZNm9Y6i5mZtUFS67t31KzsrrOWG7OdGRHbkMa1H9dGflVIi2VIXzoh4qyIGBoRQwcMWKaAbGZmy6jsQDOLdBfUu/P7y0mB5/ncZUb+/0Ihf/H2CC235mgrfWCFdDMz6yJKDTQR8W9gpqSWX62OIP2yeSLv3vpgNOmX0uT0UUq2BxbmLrZJwK75VhT9SL9enZSnLZK0fR6xNqpQlpmZdQEdcffmw4GL8v2wniA962AFYIKklof/7JfzXk8a2jyDNLz5EICImC/pZNJNBSHdAnt+fv0t3h3efEP+M7Me7M0332TWrFm89lrNd7K3rG/fvgwcOJA+ffo0rMwedwuaoUOHhgcDmDW3J598ktVWW43+/fsjVbqUa5VEBPPmzWPRokVsuummS02TND0ihi5Lub4zgJk1nddee81BZhlIon///g0/E3SgMbOm5CCzbMpoNwcaMzMrVTM/ytnMDIBNjruuoeU9ddqeDS2v2TnQNECjV+KyeOMw6ziSOProo/n5z38OwM9+9jNefvllxo4du9xln3feeUybNo1f//rXy11WR3DXmZlZCVZaaSWuuOIK5s6d237mJudAY2ZWgt69ezNmzBhOP/3090x7+umnGTFiBFtttRUjRozgmWeeqVrOZZddxpZbbsmQIUMYPnz4O+mzZ89m5MiRDBo0iO9///vvpF988cV89KMfZcstt+TYY48FYMKECRx99NEAnHHGGWy22WYAPP7443zyk59syPK2xYHGzKwkhx12GBdddBELFy5cKv3b3/42o0aN4oEHHuCggw7iiCOOqFrGSSedxKRJk7j//vuZOHHiO+n33Xcfl156KQ8++CCXXnopM2fOZPbs2Rx77LHcdNNN3HfffUydOpWrrrqK4cOHM2XKFACmTJlC//79efbZZ7n99tvZaaedyln4AgcaM7OSrL766owaNYpx48YtlX7nnXdy4IEHAnDwwQdz++23Vy1jxx135Ctf+Qp/+MMfWLJkyTvpI0aMYI011qBv374MHjyYp59+mqlTp7LzzjszYMAAevfuzUEHHcRtt93G+9//fl5++WUWLVrEzJkzOfDAA7ntttuYMmWKA42ZWXd31FFHcfbZZ7N48eKqedr67crvfvc7fvzjHzNz5ky23npr5s2bB6RrQC169erFW2+9RVt3evnEJz7Bueeey+abb85OO+3ElClTuPPOO9lxxx2XYanq41FnZtb0OnPE5VprrcUXv/hFzj77bL761a8CsMMOO3DJJZdw8MEHc9FFF7V5neTxxx9n2LBhDBs2jGuuuYaZM2dWzTts2DCOPPJI5s6dS79+/bj44os5/PDDARg+fDgnnHACJ5xwAttssw0333wzK6+8MmussUZjF7gCn9GYmZXsmGOOWWr02bhx4zj33HPZaqutuOCCCzjjjDOqzvu9733vnYv7w4cPZ8iQIVXzrrfeepx66qnssssuDBkyhG233Za9994bgJ122omZM2cyfPhwevXqxYYb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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fd2020ed6d8>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#exploring noshow with gender\n",
    "df.groupby('gender').No_show.value_counts().plot(kind='bar')\n",
    "plt.xlabel('gender_No_show')\n",
    "plt.ylabel('gender_count')\n",
    "plt.title('Patient  that did not show up with respect of their gender ')\n",
    "plt.legend();"
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
       "0.43837089475334917"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sms_received[No_show].mean()\n"
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
       "0.29133411935425357"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sms_received[did_show].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fd232598ac8>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#exploring noshow with messages received \n",
    "df.sms_received[No_show].plot(kind = 'hist',alpha= 0.5, label = 'Noshow')\n",
    "df.sms_received[did_show].plot(kind = 'hist', alpha= 0.5, label ='didshow')\n",
    "plt.xlabel('Appearance')\n",
    "plt.ylabel('sms_count')\n",
    "plt.title('Patient  that did not show up with respect of their ages ')\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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4CBgtqT+uZ+AzwFPVDMOM7P22HDDDTnhhBO48MLVX9s9depUjj32WACOP/54pkyZAsCIESM46aST+M1vfsPKlf98JfmoUaPYaKON6N27N0OGDOHFF19k+vTp7L///jQ0NNCzZ0+OO+44Jk2axIc//GGWLVvG0qVLmTdvHsceeyyTJk1i8uTJ3Sc5AP2BCZIeA6YD90bEHcDVkh4HHgf6kV6obWbW5Zx22mlcdtllvPXWW2XHaXyM9JJLLuGcc85h3rx5DB06lMWLFwPp/kWjHj16sGLFClp60dpee+3F5Zdfzvbbb8++++7L5MmTmTp1KiNGjOigUrWuqskhIh6LiGERsXNE7BgRZ+f+B0bETrnflyNiWWvzMjOrhU033ZQvfvGLXHbZZav67b333lx77bUAXH311avuBcyZM4c99tiDs88+m379+jFv3ryy891jjz2YOHEir776KitXruSaa65hv/32A2DkyJGMGzeOkSNHMmzYMCZMmMB6663HRhttVMWSrs7NZ5hZl1fJo6fVdPrpp6/2KOqFF17IV77yFX72s5/R0NDA5ZdfDsD3vvc9nn32WSKCUaNGscsuuzBz5sxm59m/f3/OPfdcDjjgACKCww47jMMPPxyAfffdl3nz5jFy5Eh69OjBFltsweDBg6tf0BJ18w7p4cOHh1/2Uwf8KKt1gFmzZrHDDjvUOoy609x6k/RQRAxv67zctpKZmRU4OZiZWYGTg5mZFTg5mJlZgZODmZkVODmYmVmBf+dgZl1fRz8i3Y7HnseOHcv666/Pm2++yciRIznooINWG37//fczbtw47rjjjmanb214V+PkYGbWBmeffXatQ+gUrlYyMyvjJz/5Cdtvvz0HHXQQTz/9NAAnnXQSN96YXmJ59913M3jwYPbZZx9uuummVdNNnDiRoUOHMnToUIYNG8bSpUsBWLZsGUcddRSDBw/muOOOW9W+0n333cewYcPYaaed+MpXvsI777zDtGnTOPLIIwG49dZb6dOnD++++y7Lly9f1Yx3NTk5mJk146GHHuLaa6/lkUce4aabbmL69OmrDV++fDlf/epXuf3225k8eTJ///vfVw0bN24cF110ETNnzmTy5Mn06dMHgEceeYQLLriAp556iueff54HHniA5cuXc9JJJ61q0nvFihVcfPHF7LrrrjzyyCNAarp7xx13ZPr0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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fd2020bf7b8>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#how age is associated  with no_show medical appointment\n",
    "df.age[No_show].value_counts().plot(kind = 'hist',alpha= 0.5, label = 'Noshow')\n",
    "df.age[did_show].value_counts().plot(kind = 'hist', alpha= 0.5, label ='didshow')\n",
    "plt.xlabel('Appearance')\n",
    "plt.ylabel('Age_count')\n",
    "plt.title('Patient  that did not show up with respect of their ages ')\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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kTXj1JF9RomIJ8mOcn+cXvsZskvi327ifTSnTds5Im4B/he4MW3Tx4CDW/jylmyDmlC40sI6OElB1kT1TCPzRpGdpNy/3QOzspC0kGwb/q3asZRL3n4paTLZBSTuJaEG+MjCzMxyOVmYmVkuN0OZmVkuH1mYmVmuDtPxW58+faJfv37VDsPMrEOZOXPmSxFRn79k8zpMsujXrx8zZsyodhhmZh2KpIb/uG8VN0OZmVkuJwszM8vlZGFmZrk6zDmLxrzzzjssWbKEVatWVTuUDqGuro6+ffvSrVu3aodiZh1Mh04WS5YsoUePHvTr14+1O660hiKC5cuXs2TJEvr371/tcMysg+nQzVCrVq2id+/eThQtIInevXv7KMzMWqVDJwvAiaIErisza60OnyzMzKzyOvQ5i4Yuu/upsq7vnAN3zF1GEqNHj+bSSy8FYOzYsaxcuZILL7ywpLKuu+46ZsyYwZVXXtmaUM3MKqpTJYtq6N69OxMnTuSCCy6gT5+W3q7bzDqcSZe0/rWfuKB8cVSJm6HaqGvXrpx66qlcdtllH5i3aNEiRowYwe67786IESN49tlnAfj973/PwIED2WOPPRg2bNia5Z9//nkOOuggdthhB84777w102+44QZ22203Bg4cyJgxYwC46aabGD16NACXX345226b3RVy3rx57L+/73FkZuXlZFEGp59+Otdffz2vvfbaWtPPOOMMTjzxRB555BGOO+44zjzzTAAuuugi7rrrLh5++GFuu23NnVuZPXs2EyZM4NFHH2XChAksXryY559/njFjxvD3v/+d2bNnM336dG699VaGDRvGlClTAJgyZQq9e/fmueeeY+rUqRxwwAHt9+bNbJ3gZFEGm2yyCSeeeCJXXHHFWtMfeOABjj32WABOOOEEpk6dCsDQoUMZNWoUV199Ne++++6a5UeMGEHPnj2pq6tjl112YdGiRUyfPp3hw4dTX19P165dOe6447jvvvv48Ic/zMqVK1mxYgWLFy/m2GOP5b777mPKlClOFmZWdk4WZXL22WdzzTXX8MYbbzS5TOHS1auuuorvf//7LF68mEGDBrF8eXZ/+u7du69ZtkuXLqxevZrmbk617777cu2117LTTjtxwAEHMGXKFB544AGGDh1apndlZpZxsiiTXr168cUvfpFrrrlmzbT99tuPG2+8EYDrr79+zbmEefPmsffee3PRRRfRp08fFi9e3OR69957b+69915eeukl3n33XW644QY+/vGPAzBs2DDGjh3LsGHD2HPPPZk0aRLdu3enZ8+eFXynZrYu6lRXQ7XkUtdKOvfcc9e69PWKK67g5JNP5kc/+hH19fVce+21AHzrW9/i6aefJiIYMWIEe+yxB7Nnz250nVtssQWXXHIJn/jEJ4gIDjnkEA4//HAADjjgABYvXsywYcPo0qULW221FQMGDKj8GzWzdU6HuQf3kCFDouHNj+bMmcPOO+9cpYg6JteZWSt10EtnJc2MiCFtXY+boczMLJeThZmZ5XKyMDOzXE4WZmaWy8nCzMxyOVmYmVmuTvU/izZd2taYEi93u/DCC9l44415/fXXGTZsGCNHjlxr/uTJkxk7dix33HFHo6/Pm29mVi0VTRaSfgkcBrwYEQPTtF7ABKAfsBD4YkS8Usk42ttFF11U7RDMzMqq0s1Q1wEHNZh2PnBPROwA3JPGO6yLL76YnXbaiZEjR/Lkk08CMGrUKG6++WYA7rzzTgYMGMD+++/PxIkT17zu3nvvZdCgQQwaNIg999yTFStWALBy5UqOOOIIBgwYwHHHHbemb6h77rmHPffck912242TTz6Zt956i2nTpvGFL3wBgD/+8Y9ssMEGvP3226xatWpNl+VmZuVQ0WQREfcBLzeYfDjwqzT8K+BzlYyhkmbOnMmNN97IrFmzmDhxItOnT19r/qpVqzjllFO4/fbbmTJlCv/617/WzBs7diw/+clPmD17NlOmTGGDDTYAYNasWYwbN44nnniC+fPn849//INVq1YxatSoNd2Xr169mp/97GcMHjyYWbNmAVk35QMHDmT69Ok8+OCD7L333u1XEWbW6VXjBPeHIuIFgPS8eRViKIspU6bw+c9/ng033JBNNtmEz372s2vNnzt3Lv3792eHHXZAEscff/yaeUOHDmX06NFcccUVvPrqq3TtmrUIfuxjH6Nv376st956DBo0iIULF/Lkk0/Sv39/dtwx6/vqpJNO4r777qNr165sv/32zJkzh2nTpjF69Gh3U25mFVHTV0NJOlXSDEkzli1bVu1wGlXodrzU+eeffz6/+MUvePPNN9lnn32YO3cuUHo35QcccAB/+ctf6NatGyNHjmTq1KlMnTp1rTvwmZm1VTWSxVJJWwCk5xebWjAi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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fd201f08b00>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#how AppointmendtDay is associated  with no_show medical appointment\n",
    "df.AppointmentDay[No_show].value_counts().plot(kind = 'hist',alpha= 0.5, label = 'Noshow', bins = 20)\n",
    "df.AppointmentDay[did_show].value_counts().plot(kind = 'hist', alpha= 0.5, label ='didshow', bins = 20)\n",
    "plt.xlabel('Appearance')\n",
    "plt.ylabel('appointment_count')\n",
    "plt.title('Patient appearance  with respect to appointment ')\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fd201f83a20>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#how schedule is associated  with no_show medical appointment \n",
    "df.schedule [No_show].value_counts().plot(kind = 'hist',alpha= 0.5, label = 'Noshow', bins = 20)\n",
    "df.schedule [did_show].value_counts().plot(kind = 'hist', alpha= 0.5, label ='didshow', bins = 20)\n",
    "plt.xlabel('Appearance')\n",
    "plt.ylabel('schedule ')\n",
    "plt.title('Patient  on schedule  with respect of their medical visit ')\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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7EmTJlV1ea3lSJ8kSeqwli1bxvHHH8/OO+/MmDFjmDlzJrvttlt9+axZsxgyZAhQfKPWN77xDYYPH87w4cOZPXs2APPnz2f8+PEMGzaMYcOGcf/99wNw1llnccIJJzBmzBiOPvpozjjjDKZMmcLgwYOZMmUK77zzDsceeyzDhg1j11135aabbgJg8uTJHHzwwYwbN44ddtiBr3/96/VtnThxIgMGDGDgwIH86Ec/AmDixIlcf/31ANx5553suuuuDBw4kGOPPZb33nuvvu1nnnkmu+22GwMHDuSpp56q+rY09EmSpA5r1qxZfOUrX2HmzJn07NmTadOm0aNHD6ZPnw7AFVdcwcSJE+vrb7LJJjz88MOceOKJfPWrXwXglFNO4Wtf+xpTp07lhhtu4Ljjjquv/8gjj3DTTTfx61//mkmTJnHYYYcxffp0DjvsMM4991z22Wcfpk6dyt13382pp57KO++8AxSHgqdMmcKMGTOYMmUKzz//PNOnT+eFF17g8ccfZ8aMGRxzzDEr9GXx4sVMnDixfr6lS5fy85//vL68V69ePProo3zpS1/i/PPPr/q2NPRJkqQOq2/fvgwePBiAIUOGMGfOHI477jiuuOIKli1bxpQpUzjiiCPq6x9++OH1Px944AEA7rjjDk488UQGDx7M/vvvz1tvvcXChQsB2H///Vl//fUbXfdtt93Geeedx+DBgxk1ahSLFy9m7ty5AIwePZoePXrQvXt3+vfvz3PPPcf222/PM888w0knncQtt9zCJptsssLynn76afr27cvHP/5xACZMmMC9995bX37wwQev0M9q85w+SZLUYa233nr1z7t168aiRYsYP348Z599Nvvssw9Dhgxh8803r69TeYXr8ufvv/8+DzzwQKPhbsMNN1zlulNK3HDDDey4444rTH/ooYdWatfSpUvZdNNNeeyxx7j11lu56KKLuPbaa7n88stXWF5z+rp8edXmSJ8kSepUunfvztixY/nSl7600iHUKVOm1P/cc889ARgzZgwXXnhhfZ3lh4Yb2njjjetHAAHGjh3LT3/60/qwNm3atNW269VXX+X9999n/PjxnHPOOTz66KMrlO+0007MmTOn/lzDX/7yl+y1117N6XJVGPokSVKnc+SRRxIRjBkzZoXp7733Hrvvvjs/+clP6i+kuOCCC6irq2PQoEH079+fiy++uNFl7r333jzxxBP1F3KcfvrpLFmyhEGDBjFgwABOP/301bbphRdeYNSoUQwePJiJEyfyve99b4Xy7t27c8UVV3DooYcycOBA1lprLb74xS+uwVZomWhqqDFHQ4cOTXV1dbVuhiRJNfPkk0/Sr1+/Wjdjlc4//3zefPNNzjnnnPppffr0oa6ujl69etWwZW2rsf0SEY+klIY2Na/n9EmSpE7loIMO4u9//zt33XVXrZvSqRj6JElSp/Lb3/620eltccVrV+I5fZIkSRkw9EmSJGXA0CdJkpQBz+mroji7yl9GvRrpTK+6liRJzWfokyRJHd5ZZ53FRhttxFtvvcXIkSPZd999V1l31KhRnH/++Qwd2uRdTIDiZs0vvvgi++23X7Wa2yEZ+iRJUpOiygezWnub4EmTJlW3IRShr66ursuHPs/pkyRJHdK5557LjjvuyL777svTTz8NwMSJE7n++uuBIgAOGzaMAQMGcMIJJ6zw3ba/+tWvGDFiBAMGDODhhx8G4J133uHYY49l2LBh7Lrrrtx0003885//5IwzzmDKlCn138TRWD2AmTNnMnz4cAYPHsygQYOYNWtWO2+RNWPokyRJHc4jjzzCNddcw7Rp0/jNb37D1KlTV6pz4oknMnXqVB5//HEWLVrE73//+/qyd955h7/+9a/87Gc/49hjjwWKELnPPvswdepU7r77bk499VSWLFnCpEmTOOyww5g+fTqHHXZYo/XeeecdLr74Yk455ZT6kcHevXu32/aoBg/vSpKkDucvf/kLBx10EBtssAEA+++//0p17r77br7//e/z7rvvsmDBAnbeeWc+97nPAXD44YcDMHLkSN566y3eeOMNbrvtNm6++WbOP/98ABYvXszcuXNXWu6q6u25556ce+65zJs3j4MPPpgddtihTfreVgx9kiSpQ4rVnEi4ePFivvzlL1NXV8c222zDWWedxeLFi1c5b0SQUuKGG25gxx13XKHsoYceWuH1qur169eP3XffnT/84Q+MHTuWSy+9lH322ae13Wt3Ht6VJEkdzsiRI/ntb3/LokWLWLhwIb/73e9WKF8e8Hr16sXbb79df57fclOmTAHgvvvuo0ePHvTo0YOxY8fy05/+tP7cv2nTpgGw8cYbs3Dhwvp5V1XvmWeeYfvtt+fkk09m//33529/+1sb9LztGPokSVKHs9tuu3HYYYcxePBgxo8fz6c+9akVynv27Mnxxx/PwIEDOfDAAxk2bNgK5ZtuuikjRozgi1/8IpdddhkAp59+OkuWLGHQoEEMGDCA008/HYC9996bJ554ov5CjlXVmzJlCgMGDGDw4ME89dRTHH300e2wJaonUmuvme7Chg4dmurq6lo8nzdnliR1FU8++ST9+vWrdTPUQGP7JSIeSSk1eVNCR/okSZIyYOiTJEnKgKFPkiQpA4Y+SZKkDBj6JEmSMmDokyRJyoChT5IkdSp9+vTh1VdfbfF8EydOXOkmzqszZ84cBgwY0OL1dFR+DZskSWqGat+L1vvNtjdH+iRJUod14IEHMmTIEHbeeWcuueSSlcqvuuoqBg0axC677MJRRx0FwHPPPcfo0aMZNGgQo0ePZu7cufX17733XkaMGMH2229fP+qXUuLUU09lwIABDBw4sP4r3LoaR/okSVKHdfnll7PZZpuxaNEihg0bxvjx4+vLZs6cybnnnsv9999Pr169WLBgAQAnnngiRx99NBMmTODyyy/n5JNP5sYbbwTgpZde4r777uOpp55i//3355BDDuE3v/kN06dP57HHHuPVV19l2LBhjBw5sib9bUuO9EmSpA7rggsuYJdddmGPPfbg+eefZ9asWfVld911F4cccgi9evUCYLPNNgPggQce4IgjjgDgqKOO4r777quf58ADD2Sttdaif//+vPzyywDcd999HH744XTr1o0tt9ySvfbai6lTp7ZXF9uNI32SJKlDuueee7jjjjt44IEH2GCDDRg1ahSLFy+uL08pEdH0uYaVddZbb70V5q/82dU50idJkjqkN998k0033ZQNNtiAp556igcffHCF8tGjR3Pttdfy2muvAdQf3h0xYgTXXHMNAFdffTWf/OQnV7uekSNHMmXKFJYtW8b8+fO59957GT58eBv0qLYc6ZMkSR3SuHHjuPjiixk0aBA77rgje+yxxwrlO++8M9/+9rfZa6+96NatG7vuuiuTJ0/mggsu4Nhjj+UHP/gBW2yxBVdcccVq13PQQQfxwAMPsMsuuxARfP/73+fDH/4wc+bMacPetb/IZUizJYYOHZrq6upaPF+cXe3L2Vctnel+kyS1nSeffJJ+/frVuhlqoLH9EhGPpJSGNjWvh3clSZIyYOiTJEnKgKFPkiQpA4Y+SZKkDBj6JEmS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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fd201ec1320>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#deduction on No_show  medical appointment  with  relation to ailments\n",
    "df.groupby('No_show').hypertension.value_counts().plot(kind='bar',figsize=(10,9) , color = 'red')\n",
    "df.groupby('No_show').diabetes.value_counts().plot(kind= 'bar', figsize=(10,9), color = 'blue');\n",
    "df.groupby('No_show').alcohol.value_counts().plot(kind= 'bar', figsize=(10,9) ,color = 'yellow');\n",
    "df.groupby('No_show').handicap.value_counts().plot(kind='Bar',figsize=(10,9),color='green');\n",
    "plt.xlabel('NO_SHOW', fontsize = 20)\n",
    "plt.ylabel('Count', fontsize =20)\n",
    "plt.title('People That  Make Appointment  In Relation   To Diseases')\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  Conclusions\n",
    "   In my findings, if I found that the dataset contains no duplications neither a null values,the No_show up column was replace with 1's and 0's for better exploration insteads of yes and no expressions. I drop some columns because i found them not useful ,They are various factor that influence if a patients will no_show or didshow for their scheduled medical appointments.\n",
    "   The gender is one of the factor observed if it can affect the schedule appointment,as shown in in[12] more female patients did show for their appointment as compared the male patents,same can be conclude  with female No_show patients.More patients didshow based on sms_count as compared to no_show but the average of  no_show patients is more to did show patients\n",
    "    Another factor I used in exploration was age. the most common age brackets for didshow  for appointment is almost 35years old while the age brackets for noshow is almost 30years old. patients that  makeit to their appointments day as noshow patient is more that did show patients . patienTs  schedule in term of noshow was higher than  didshow .\n",
    "   finally  based on  patients ailments grouping, handicap has the highest number  of didshow patients follow by alcohol, hypetension and diabetes in that order while  the handicap had the highest number of Noshow patient"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### reference \n",
    "stack overflow,\n",
    "project walkthrough\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from subprocess import call\n",
    "call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])"
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
