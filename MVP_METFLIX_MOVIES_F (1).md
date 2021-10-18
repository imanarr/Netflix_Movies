{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e0f8e375",
   "metadata": {},
   "source": [
    "# Importing library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ad403e57",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import plotly.express as px\n",
    "import plotly.graph_objects as go\n",
    "from plotly.subplots import make_subplots\n",
    "import plotly.figure_factory as ff\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly.graph_objects as go\n",
    "from plotly.offline import init_notebook_mode, iplot\n",
    "import pandas as pd \n",
    "import seaborn as sns\n",
    "import plotly.express as px\n",
    "from sklearn.cluster import KMeans\n",
    "import re\n",
    "from gensim.models.fasttext import FastText as FT_gensim\n",
    "from sklearn.cluster import KMeans\n",
    "from scipy.spatial.distance import cdist\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "96f10c33",
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
       "      <th>show_id</th>\n",
       "      <th>type</th>\n",
       "      <th>title</th>\n",
       "      <th>director</th>\n",
       "      <th>cast</th>\n",
       "      <th>country</th>\n",
       "      <th>date_added</th>\n",
       "      <th>release_year</th>\n",
       "      <th>rating</th>\n",
       "      <th>duration</th>\n",
       "      <th>listed_in</th>\n",
       "      <th>description</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>s1</td>\n",
       "      <td>Movie</td>\n",
       "      <td>Dick Johnson Is Dead</td>\n",
       "      <td>Kirsten Johnson</td>\n",
       "      <td>NaN</td>\n",
       "      <td>United States</td>\n",
       "      <td>September 25, 2021</td>\n",
       "      <td>2020</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>90 min</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>As her father nears the end of his life, filmm...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>s2</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Blood &amp; Water</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>\n",
       "      <td>South Africa</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>2 Seasons</td>\n",
       "      <td>International TV Shows, TV Dramas, TV Mysteries</td>\n",
       "      <td>After crossing paths at a party, a Cape Town t...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>s3</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Ganglands</td>\n",
       "      <td>Julien Leclercq</td>\n",
       "      <td>Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>1 Season</td>\n",
       "      <td>Crime TV Shows, International TV Shows, TV Act...</td>\n",
       "      <td>To protect his family from a powerful drug lor...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>s4</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Jailbirds New Orleans</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>1 Season</td>\n",
       "      <td>Docuseries, Reality TV</td>\n",
       "      <td>Feuds, flirtations and toilet talk go down amo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>s5</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Kota Factory</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>\n",
       "      <td>India</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>2 Seasons</td>\n",
       "      <td>International TV Shows, Romantic TV Shows, TV ...</td>\n",
       "      <td>In a city of coaching centers known to train I...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>s6</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>Midnight Mass</td>\n",
       "      <td>Mike Flanagan</td>\n",
       "      <td>Kate Siegel, Zach Gilford, Hamish Linklater, H...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>1 Season</td>\n",
       "      <td>TV Dramas, TV Horror, TV Mysteries</td>\n",
       "      <td>The arrival of a charismatic young priest brin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>s7</td>\n",
       "      <td>Movie</td>\n",
       "      <td>My Little Pony: A New Generation</td>\n",
       "      <td>Robert Cullen, José Luis Ucha</td>\n",
       "      <td>Vanessa Hudgens, Kimiko Glenn, James Marsden, ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>PG</td>\n",
       "      <td>91 min</td>\n",
       "      <td>Children &amp; Family Movies</td>\n",
       "      <td>Equestria's divided. But a bright-eyed hero be...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>s8</td>\n",
       "      <td>Movie</td>\n",
       "      <td>Sankofa</td>\n",
       "      <td>Haile Gerima</td>\n",
       "      <td>Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...</td>\n",
       "      <td>United States, Ghana, Burkina Faso, United Kin...</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>1993</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>125 min</td>\n",
       "      <td>Dramas, Independent Movies, International Movies</td>\n",
       "      <td>On a photo shoot in Ghana, an American model s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>s9</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>The Great British Baking Show</td>\n",
       "      <td>Andy Devonshire</td>\n",
       "      <td>Mel Giedroyc, Sue Perkins, Mary Berry, Paul Ho...</td>\n",
       "      <td>United Kingdom</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>TV-14</td>\n",
       "      <td>9 Seasons</td>\n",
       "      <td>British TV Shows, Reality TV</td>\n",
       "      <td>A talented batch of amateur bakers face off in...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>s10</td>\n",
       "      <td>Movie</td>\n",
       "      <td>The Starling</td>\n",
       "      <td>Theodore Melfi</td>\n",
       "      <td>Melissa McCarthy, Chris O'Dowd, Kevin Kline, T...</td>\n",
       "      <td>United States</td>\n",
       "      <td>September 24, 2021</td>\n",
       "      <td>2021</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>104 min</td>\n",
       "      <td>Comedies, Dramas</td>\n",
       "      <td>A woman adjusting to life after a loss contend...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  show_id     type                             title  \\\n",
       "0      s1    Movie              Dick Johnson Is Dead   \n",
       "1      s2  TV Show                     Blood & Water   \n",
       "2      s3  TV Show                         Ganglands   \n",
       "3      s4  TV Show             Jailbirds New Orleans   \n",
       "4      s5  TV Show                      Kota Factory   \n",
       "5      s6  TV Show                     Midnight Mass   \n",
       "6      s7    Movie  My Little Pony: A New Generation   \n",
       "7      s8    Movie                           Sankofa   \n",
       "8      s9  TV Show     The Great British Baking Show   \n",
       "9     s10    Movie                      The Starling   \n",
       "\n",
       "                        director  \\\n",
       "0                Kirsten Johnson   \n",
       "1                            NaN   \n",
       "2                Julien Leclercq   \n",
       "3                            NaN   \n",
       "4                            NaN   \n",
       "5                  Mike Flanagan   \n",
       "6  Robert Cullen, José Luis Ucha   \n",
       "7                   Haile Gerima   \n",
       "8                Andy Devonshire   \n",
       "9                 Theodore Melfi   \n",
       "\n",
       "                                                cast  \\\n",
       "0                                                NaN   \n",
       "1  Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...   \n",
       "2  Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...   \n",
       "3                                                NaN   \n",
       "4  Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...   \n",
       "5  Kate Siegel, Zach Gilford, Hamish Linklater, H...   \n",
       "6  Vanessa Hudgens, Kimiko Glenn, James Marsden, ...   \n",
       "7  Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...   \n",
       "8  Mel Giedroyc, Sue Perkins, Mary Berry, Paul Ho...   \n",
       "9  Melissa McCarthy, Chris O'Dowd, Kevin Kline, T...   \n",
       "\n",
       "                                             country          date_added  \\\n",
       "0                                      United States  September 25, 2021   \n",
       "1                                       South Africa  September 24, 2021   \n",
       "2                                                NaN  September 24, 2021   \n",
       "3                                                NaN  September 24, 2021   \n",
       "4                                              India  September 24, 2021   \n",
       "5                                                NaN  September 24, 2021   \n",
       "6                                                NaN  September 24, 2021   \n",
       "7  United States, Ghana, Burkina Faso, United Kin...  September 24, 2021   \n",
       "8                                     United Kingdom  September 24, 2021   \n",
       "9                                      United States  September 24, 2021   \n",
       "\n",
       "   release_year rating   duration  \\\n",
       "0          2020  PG-13     90 min   \n",
       "1          2021  TV-MA  2 Seasons   \n",
       "2          2021  TV-MA   1 Season   \n",
       "3          2021  TV-MA   1 Season   \n",
       "4          2021  TV-MA  2 Seasons   \n",
       "5          2021  TV-MA   1 Season   \n",
       "6          2021     PG     91 min   \n",
       "7          1993  TV-MA    125 min   \n",
       "8          2021  TV-14  9 Seasons   \n",
       "9          2021  PG-13    104 min   \n",
       "\n",
       "                                           listed_in  \\\n",
       "0                                      Documentaries   \n",
       "1    International TV Shows, TV Dramas, TV Mysteries   \n",
       "2  Crime TV Shows, International TV Shows, TV Act...   \n",
       "3                             Docuseries, Reality TV   \n",
       "4  International TV Shows, Romantic TV Shows, TV ...   \n",
       "5                 TV Dramas, TV Horror, TV Mysteries   \n",
       "6                           Children & Family Movies   \n",
       "7   Dramas, Independent Movies, International Movies   \n",
       "8                       British TV Shows, Reality TV   \n",
       "9                                   Comedies, Dramas   \n",
       "\n",
       "                                         description  \n",
       "0  As her father nears the end of his life, filmm...  \n",
       "1  After crossing paths at a party, a Cape Town t...  \n",
       "2  To protect his family from a powerful drug lor...  \n",
       "3  Feuds, flirtations and toilet talk go down amo...  \n",
       "4  In a city of coaching centers known to train I...  \n",
       "5  The arrival of a charismatic young priest brin...  \n",
       "6  Equestria's divided. But a bright-eyed hero be...  \n",
       "7  On a photo shoot in Ghana, an American model s...  \n",
       "8  A talented batch of amateur bakers face off in...  \n",
       "9  A woman adjusting to life after a loss contend...  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df =  pd.read_csv(\"netflix_titles.csv\")\n",
    "df.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba95333d",
   "metadata": {},
   "source": [
    "## Data Exploration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5da76764",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 8807 entries, 0 to 8806\n",
      "Data columns (total 12 columns):\n",
      " #   Column        Non-Null Count  Dtype \n",
      "---  ------        --------------  ----- \n",
      " 0   show_id       8807 non-null   object\n",
      " 1   type          8807 non-null   object\n",
      " 2   title         8807 non-null   object\n",
      " 3   director      6173 non-null   object\n",
      " 4   cast          7982 non-null   object\n",
      " 5   country       7976 non-null   object\n",
      " 6   date_added    8797 non-null   object\n",
      " 7   release_year  8807 non-null   int64 \n",
      " 8   rating        8803 non-null   object\n",
      " 9   duration      8804 non-null   object\n",
      " 10  listed_in     8807 non-null   object\n",
      " 11  description   8807 non-null   object\n",
      "dtypes: int64(1), object(11)\n",
      "memory usage: 825.8+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7fe60f8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "show_id            0\n",
       "type               0\n",
       "title              0\n",
       "director        2634\n",
       "cast             825\n",
       "country          831\n",
       "date_added        10\n",
       "release_year       0\n",
       "rating             4\n",
       "duration           3\n",
       "listed_in          0\n",
       "description        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find the nulls value\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "60d9c992",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "show_id         8807\n",
       "type               2\n",
       "title           8807\n",
       "director        4528\n",
       "cast            7692\n",
       "country          748\n",
       "date_added      1767\n",
       "release_year      74\n",
       "rating            17\n",
       "duration         220\n",
       "listed_in        514\n",
       "description     8775\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find the unique value\n",
    "df.nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b109f1d",
   "metadata": {},
   "source": [
    "#  Data Cleaning\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "51aa4f7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3472"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Replace null values with Null\n",
    "df['country'].fillna('Null',inplace=True)\n",
    "df['rating'].fillna('Null',inplace=True)\n",
    "df.isnull().sum().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6b1e82b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "show_id            0\n",
       "type               0\n",
       "title              0\n",
       "director        2634\n",
       "cast             825\n",
       "country            0\n",
       "date_added        10\n",
       "release_year       0\n",
       "rating             0\n",
       "duration           3\n",
       "listed_in          0\n",
       "description        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b5dd9abc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Converting into date-time format and adding two more features year and month.\n",
    "\n",
    "df[\"date_added\"] = pd.to_datetime(df['date_added'])\n",
    "df['year_added'] = df['date_added'].dt.year\n",
    "df['month_added'] = df['date_added'].dt.month"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f8e2d8d",
   "metadata": {},
   "source": [
    "# Data Visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "235c2052",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 792x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Heatmap\n",
    "# Correlation between the features\n",
    "month_year_df = df.groupby('year_added')['month_added'].value_counts().unstack().fillna(0).T\n",
    "\n",
    "plt.figure(figsize=(11,8))\n",
    "sns.heatmap(month_year_df, linewidths=0.025, cmap=\"Greens\")\n",
    "plt.title(\"Content Heatmap\")\n",
    "plt.ylabel(\"Month\")\n",
    "plt.xlabel(\"Year\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "58c41fb6",
   "metadata": {},
   "outputs": [
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
    "# Create the years and durations lists\n",
    "years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]\n",
    "durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]\n",
    "\n",
    "# Create a dictionary with the two lists\n",
    "movie_dict = {'years': years, 'durations': durations}\n",
    "\n",
    "# Draw a line plot of release_years and durations\n",
    "line =plt.plot(years, durations , linewidth = 1 , color='g')\n",
    "\n",
    "# Create a title\n",
    "plt.title('Netflix Movie Durations 2011-2020',fontsize = 20,style='italic',weight='bold',rotation=0,color='purple');\n",
    "plt.xlabel('YEARS',fontsize = 8, weight = 'bold',color='green');\n",
    "plt.ylabel('MOVIE DURATIONS',fontsize = 8, weight = 'bold',color='green');\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f5dc92e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.02, 'Persentage of Content Type')"
      ]
     },
     "execution_count": 19,
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
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot Pie chart to show the percentage of content type\n",
    "df['type'].value_counts().plot(kind='pie', autopct='%1.0f%%', legend=dict(x=0.1, y=1.1))\n",
    "plt.title(\"Persentage of Content Type\", y=1.02 , fontsize = 10,style='italic',weight='bold',rotation=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "ebebb9b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 504x648 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data = df.set_index('title').country.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);\n",
    "\n",
    "plt.figure(figsize=(7,9))\n",
    "g = sns.countplot(y = data, order=data.value_counts().index[:20] , palette= [\"#7fcdbb\",\"#edf8b1\"])\n",
    "plt.title('Top 20 Countries on Netflix' , family='serif',fontsize = 15,loc='center',color='r');\n",
    "plt.xlabel('Titles')\n",
    "plt.ylabel('Country')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "62f7c681",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "marker": {
          "color": "#EC7063"
         },
         "name": "TV Shows",
         "type": "scatter",
         "x": [
          2008,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          1,
          5,
          5,
          26,
          176,
          349,
          412,
          592,
          595,
          505
         ]
        },
        {
         "marker": {
          "color": "#1D8348"
         },
         "name": "Movies",
         "type": "scatter",
         "x": [
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020,
          2021
         ],
         "y": [
          1,
          2,
          1,
          13,
          3,
          6,
          19,
          56,
          253,
          839,
          1237,
          1424,
          1284,
          993
         ]
        }
       ],
       "layout": {
        "legend": {
         "orientation": "h",
         "x": 0.1,
         "y": 1.1
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Content added over the years"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"6e8fdeee-bc5d-4570-abea-d2ba6d88f49e\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"6e8fdeee-bc5d-4570-abea-d2ba6d88f49e\")) {                    Plotly.newPlot(                        \"6e8fdeee-bc5d-4570-abea-d2ba6d88f49e\",                        [{\"marker\":{\"color\":\"#EC7063\"},\"name\":\"TV Shows\",\"type\":\"scatter\",\"x\":[2008.0,2013.0,2014.0,2015.0,2016.0,2017.0,2018.0,2019.0,2020.0,2021.0],\"y\":[1,5,5,26,176,349,412,592,595,505]},{\"marker\":{\"color\":\"#1D8348\"},\"name\":\"Movies\",\"type\":\"scatter\",\"x\":[2008.0,2009.0,2010.0,2011.0,2012.0,2013.0,2014.0,2015.0,2016.0,2017.0,2018.0,2019.0,2020.0,2021.0],\"y\":[1,2,1,13,3,6,19,56,253,839,1237,1424,1284,993]}],                        {\"legend\":{\"orientation\":\"h\",\"x\":0.1,\"y\":1.1},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"Content added over the years\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('6e8fdeee-bc5d-4570-abea-d2ba6d88f49e');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#How does the timeline look like for the addition of International Movies compared to International TV Shows?\n",
    "d1 = df[df[\"type\"] == \"TV Show\"]\n",
    "d2 = df[df[\"type\"] == \"Movie\"]\n",
    "\n",
    "col = \"year_added\"\n",
    "\n",
    "X1 = d1[col].value_counts().reset_index()\n",
    "X1 = X1.rename(columns = {col : \"count\", \"index\" : col})\n",
    "X1['percent'] = X1['count'].apply(lambda x : 100*x/sum(X1['count']))\n",
    "X1 = X1.sort_values(col)\n",
    "\n",
    "\n",
    "Y2 = d2[col].value_counts().reset_index()\n",
    "Y2 = Y2.rename(columns = {col : \"count\", \"index\" : col})\n",
    "Y2['percent'] = Y2['count'].apply(lambda x : 100*x/sum(Y2['count']))\n",
    "Y2 = Y2.sort_values(col)\n",
    "\n",
    "\n",
    "new_x = go.Scatter(x=X1[col], y=X1[\"count\"], name=\"TV Shows\", marker=dict(color=\"#EC7063\"))\n",
    "new_y = go.Scatter(x=Y2[col], y=Y2[\"count\"], name=\"Movies\", marker=dict(color=\"#1D8348\"))\n",
    "data = [new_x, new_y]\n",
    "layout = go.Layout(title=\"Content added over the years\",legend=dict(x=0.1, y=1.1, orientation=\"h\"))\n",
    "fig = go.Figure(data, layout=layout)\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "6fb399de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "order =  ['G', 'TV-Y', 'TV-G', 'PG', 'TV-Y7', 'TV-Y7-FV', 'TV-PG', 'PG-13', 'TV-14', 'R', 'NC-17', 'TV-MA']\n",
    "plt.figure(figsize=(15,7))\n",
    "g = sns.countplot(df.rating, hue=df.type, order=order, palette= [\"#7fcdbb\",\"#edf8b1\"] );\n",
    "plt.title(\"Ratings for Movies & TV Shows\")\n",
    "plt.xlabel(\"Rating\")\n",
    "plt.ylabel(\"Total Count\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d2156412",
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
       "      <th>title</th>\n",
       "      <th>listed_in</th>\n",
       "      <th>description</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Dick Johnson Is Dead</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>As her father nears the end of his life, filmm...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>My Little Pony: A New Generation</td>\n",
       "      <td>Children &amp; Family Movies</td>\n",
       "      <td>Equestria's divided. But a bright-eyed hero be...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Sankofa</td>\n",
       "      <td>Dramas, Independent Movies, International Movies</td>\n",
       "      <td>On a photo shoot in Ghana, an American model s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>The Starling</td>\n",
       "      <td>Comedies, Dramas</td>\n",
       "      <td>A woman adjusting to life after a loss contend...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Je Suis Karl</td>\n",
       "      <td>Dramas, International Movies</td>\n",
       "      <td>After most of her family is murdered in a terr...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              title  \\\n",
       "0              Dick Johnson Is Dead   \n",
       "1  My Little Pony: A New Generation   \n",
       "2                           Sankofa   \n",
       "3                      The Starling   \n",
       "4                      Je Suis Karl   \n",
       "\n",
       "                                          listed_in  \\\n",
       "0                                     Documentaries   \n",
       "1                          Children & Family Movies   \n",
       "2  Dramas, Independent Movies, International Movies   \n",
       "3                                  Comedies, Dramas   \n",
       "4                      Dramas, International Movies   \n",
       "\n",
       "                                         description  \n",
       "0  As her father nears the end of his life, filmm...  \n",
       "1  Equestria's divided. But a bright-eyed hero be...  \n",
       "2  On a photo shoot in Ghana, an American model s...  \n",
       "3  A woman adjusting to life after a loss contend...  \n",
       "4  After most of her family is murdered in a terr...  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df[df[\"type\"] == \"Movie\"].reset_index()\n",
    "netflix = df[[\"title\", \"listed_in\", \"description\"]].copy()\n",
    "netflix.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "21f698bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocessing(text):\n",
    "    text = text.lower()\n",
    "    text = re.sub('[-=+,#/\\?:^$.@*\\\"※~&%ㆍ!』\\\\‘|\\(\\)\\[\\]\\<\\>`\\'…》]', ' ', text)\n",
    "    text = \" \".join(text.split())\n",
    "    \n",
    "    return text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4386792f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6131, 5)\n"
     ]
    },
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
       "      <th>title</th>\n",
       "      <th>listed_in</th>\n",
       "      <th>description</th>\n",
       "      <th>new_description</th>\n",
       "      <th>new_desc</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Dick Johnson Is Dead</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>As her father nears the end of his life, filmm...</td>\n",
       "      <td>as her father nears the end of his life filmma...</td>\n",
       "      <td>as her father nears the end of his life filmma...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>My Little Pony: A New Generation</td>\n",
       "      <td>Children &amp; Family Movies</td>\n",
       "      <td>Equestria's divided. But a bright-eyed hero be...</td>\n",
       "      <td>equestria s divided but a bright eyed hero bel...</td>\n",
       "      <td>equestria s divided but a bright eyed hero bel...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Sankofa</td>\n",
       "      <td>Dramas, Independent Movies, International Movies</td>\n",
       "      <td>On a photo shoot in Ghana, an American model s...</td>\n",
       "      <td>on a photo shoot in ghana an american model sl...</td>\n",
       "      <td>on a photo shoot in ghana an american model sl...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>The Starling</td>\n",
       "      <td>Comedies, Dramas</td>\n",
       "      <td>A woman adjusting to life after a loss contend...</td>\n",
       "      <td>a woman adjusting to life after a loss contend...</td>\n",
       "      <td>a woman adjusting to life after a loss contend...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Je Suis Karl</td>\n",
       "      <td>Dramas, International Movies</td>\n",
       "      <td>After most of her family is murdered in a terr...</td>\n",
       "      <td>after most of her family is murdered in a terr...</td>\n",
       "      <td>after most of her family is murdered in a terr...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              title  \\\n",
       "0              Dick Johnson Is Dead   \n",
       "1  My Little Pony: A New Generation   \n",
       "2                           Sankofa   \n",
       "3                      The Starling   \n",
       "4                      Je Suis Karl   \n",
       "\n",
       "                                          listed_in  \\\n",
       "0                                     Documentaries   \n",
       "1                          Children & Family Movies   \n",
       "2  Dramas, Independent Movies, International Movies   \n",
       "3                                  Comedies, Dramas   \n",
       "4                      Dramas, International Movies   \n",
       "\n",
       "                                         description  \\\n",
       "0  As her father nears the end of his life, filmm...   \n",
       "1  Equestria's divided. But a bright-eyed hero be...   \n",
       "2  On a photo shoot in Ghana, an American model s...   \n",
       "3  A woman adjusting to life after a loss contend...   \n",
       "4  After most of her family is murdered in a terr...   \n",
       "\n",
       "                                     new_description  \\\n",
       "0  as her father nears the end of his life filmma...   \n",
       "1  equestria s divided but a bright eyed hero bel...   \n",
       "2  on a photo shoot in ghana an american model sl...   \n",
       "3  a woman adjusting to life after a loss contend...   \n",
       "4  after most of her family is murdered in a terr...   \n",
       "\n",
       "                                            new_desc  \n",
       "0  as her father nears the end of his life filmma...  \n",
       "1  equestria s divided but a bright eyed hero bel...  \n",
       "2  on a photo shoot in ghana an american model sl...  \n",
       "3  a woman adjusting to life after a loss contend...  \n",
       "4  after most of her family is murdered in a terr...  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix[\"new_desc\"] = netflix[\"description\"].apply(lambda x: preprocessing(x))\n",
    "print(netflix.shape)\n",
    "netflix.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "ec7db8c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "as her father nears the end of his life filmmaker kirsten johnson stages his death in inventive and comical ways to help them both face the inevitable\n",
      "['as', 'her', 'father', 'nears', 'the', 'end', 'of', 'his', 'life', 'filmmaker', 'kirsten', 'johnson', 'stages', 'his', 'death', 'in', 'inventive', 'and', 'comical', 'ways', 'to', 'help', 'them', 'both', 'face', 'the', 'inevitable']\n"
     ]
    }
   ],
   "source": [
    "corpus = netflix[\"new_desc\"].tolist()\n",
    "word = [re.split(' ', str(word)) for word in corpus]\n",
    "print(corpus[0])\n",
    "print(word[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4846121",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b1b9f03b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Count corpus :  6131\n",
      "Total words corpus:  151843\n",
      "FastText(vocab=8454, vector_size=30, alpha=0.025)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "embedding_size = 30\n",
    "\n",
    "model = FT_gensim(vector_size=embedding_size, min_count=2, min_n=2, max_n=5, sg=1, negative=10,\n",
    "                         sample=0.001, window=5, alpha=0.025, min_alpha=0.0001, epochs=50)\n",
    "model.build_vocab(word)\n",
    "\n",
    "\n",
    "print('Count corpus : ', model.corpus_count)\n",
    "print('Total words corpus: ', model.corpus_total_words)\n",
    "\n",
    "model.train(sentences,\n",
    "    epochs=FT_model.epochs,\n",
    "    total_examples=model.corpus_count, total_words=model.corpus_total_words)\n",
    "\n",
    "print(model)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "fe1f15b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "vector = []\n",
    "\n",
    "for item in corpus:\n",
    "        vector.append(model.wv[str(item)])\n",
    "vector = np.asarray(vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "c8c2ec7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "kmeanModel = KMeans(n_clusters=50, random_state=42).fit(vector)\n",
    "cluster_no = kmeanModel.predict(vector)\n",
    "netflix[\"cluster_no\"] = cluster_no"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "6d13530f",
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
       "      <th>title</th>\n",
       "      <th>listed_in</th>\n",
       "      <th>description</th>\n",
       "      <th>new_description</th>\n",
       "      <th>new_desc</th>\n",
       "      <th>cluster_id</th>\n",
       "      <th>cluster_no</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Dick Johnson Is Dead</td>\n",
       "      <td>Documentaries</td>\n",
       "      <td>As her father nears the end of his life, filmm...</td>\n",
       "      <td>as her father nears the end of his life filmma...</td>\n",
       "      <td>as her father nears the end of his life filmma...</td>\n",
       "      <td>24</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>My Little Pony: A New Generation</td>\n",
       "      <td>Children &amp; Family Movies</td>\n",
       "      <td>Equestria's divided. But a bright-eyed hero be...</td>\n",
       "      <td>equestria s divided but a bright eyed hero bel...</td>\n",
       "      <td>equestria s divided but a bright eyed hero bel...</td>\n",
       "      <td>26</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Sankofa</td>\n",
       "      <td>Dramas, Independent Movies, International Movies</td>\n",
       "      <td>On a photo shoot in Ghana, an American model s...</td>\n",
       "      <td>on a photo shoot in ghana an american model sl...</td>\n",
       "      <td>on a photo shoot in ghana an american model sl...</td>\n",
       "      <td>16</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>The Starling</td>\n",
       "      <td>Comedies, Dramas</td>\n",
       "      <td>A woman adjusting to life after a loss contend...</td>\n",
       "      <td>a woman adjusting to life after a loss contend...</td>\n",
       "      <td>a woman adjusting to life after a loss contend...</td>\n",
       "      <td>18</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Je Suis Karl</td>\n",
       "      <td>Dramas, International Movies</td>\n",
       "      <td>After most of her family is murdered in a terr...</td>\n",
       "      <td>after most of her family is murdered in a terr...</td>\n",
       "      <td>after most of her family is murdered in a terr...</td>\n",
       "      <td>40</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              title  \\\n",
       "0              Dick Johnson Is Dead   \n",
       "1  My Little Pony: A New Generation   \n",
       "2                           Sankofa   \n",
       "3                      The Starling   \n",
       "4                      Je Suis Karl   \n",
       "\n",
       "                                          listed_in  \\\n",
       "0                                     Documentaries   \n",
       "1                          Children & Family Movies   \n",
       "2  Dramas, Independent Movies, International Movies   \n",
       "3                                  Comedies, Dramas   \n",
       "4                      Dramas, International Movies   \n",
       "\n",
       "                                         description  \\\n",
       "0  As her father nears the end of his life, filmm...   \n",
       "1  Equestria's divided. But a bright-eyed hero be...   \n",
       "2  On a photo shoot in Ghana, an American model s...   \n",
       "3  A woman adjusting to life after a loss contend...   \n",
       "4  After most of her family is murdered in a terr...   \n",
       "\n",
       "                                     new_description  \\\n",
       "0  as her father nears the end of his life filmma...   \n",
       "1  equestria s divided but a bright eyed hero bel...   \n",
       "2  on a photo shoot in ghana an american model sl...   \n",
       "3  a woman adjusting to life after a loss contend...   \n",
       "4  after most of her family is murdered in a terr...   \n",
       "\n",
       "                                            new_desc  cluster_id  cluster_no  \n",
       "0  as her father nears the end of his life filmma...          24          45  \n",
       "1  equestria s divided but a bright eyed hero bel...          26          22  \n",
       "2  on a photo shoot in ghana an american model sl...          16          45  \n",
       "3  a woman adjusting to life after a loss contend...          18          45  \n",
       "4  after most of her family is murdered in a terr...          40          37  "
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "b213e86b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recommendation_system(title_name):\n",
    "    top_k = 5\n",
    "    title_row = netflix[netflix[\"title\"] == title_name].copy()\n",
    "    search_df = netflix[netflix[\"cluster_id\"].isin(title_row[\"cluster_id\"])].copy()\n",
    "    search_df = search_df.drop(search_df[search_df[\"title\"] == title_name].index)\n",
    "    \n",
    "    search_df[\"Similarity\"] = search_df.apply(lambda x: FT_model.wv.similarity(title_row[\"new_description\"], x[\"new_description\"]), axis=1)\n",
    "    search_df.sort_values(by=[\"Similarity\"], ascending=False, inplace=True)\n",
    "    \n",
    "    return search_df[[\"title\", \"Similarity\"]].head(top_k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "ac968f4f",
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
       "      <th>title</th>\n",
       "      <th>Similarity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>935</th>\n",
       "      <td>Apaharan</td>\n",
       "      <td>[0.9646945]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2138</th>\n",
       "      <td>Shadow</td>\n",
       "      <td>[0.96063566]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3632</th>\n",
       "      <td>Sarajevo</td>\n",
       "      <td>[0.95412594]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>578</th>\n",
       "      <td>Nayattu</td>\n",
       "      <td>[0.95323175]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5948</th>\n",
       "      <td>Three-Quarters Decent</td>\n",
       "      <td>[0.95286036]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      title    Similarity\n",
       "935                Apaharan   [0.9646945]\n",
       "2138                 Shadow  [0.96063566]\n",
       "3632               Sarajevo  [0.95412594]\n",
       "578                 Nayattu  [0.95323175]\n",
       "5948  Three-Quarters Decent  [0.95286036]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recommendation_system(\"Aakhri Adaalat\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8264038e",
   "metadata": {},
   "outputs": [],
   "source": [
    "recommendation_system(\"National Parks Adventure\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5638bd3f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.8.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
