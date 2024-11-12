{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO1zIWHSzAi3NteGBhFPp1q",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ro-shni/MERCARI/blob/main/Mercari.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"\"\n",
        "identifier = \"com.mercariapp.mercari\"\n",
        "country = \"us\"\n",
        "lookup_period = \"365d\" #200reviews\n"
      ],
      "metadata": {
        "id": "7xIvPXwzejbq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_o4DCORUeUpM",
        "outputId": "eec53e8d-eee7-49ef-e438-ee6b9edbf1b4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting google-play-scraper\n",
            "  Downloading google_play_scraper-1.2.7-py3-none-any.whl.metadata (50 kB)\n",
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/50.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m50.2/50.2 kB\u001b[0m \u001b[31m1.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (2.2.2)\n",
            "Requirement already satisfied: numpy>=1.22.4 in /usr/local/lib/python3.10/dist-packages (from pandas) (1.26.4)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
            "Downloading google_play_scraper-1.2.7-py3-none-any.whl (28 kB)\n",
            "Installing collected packages: google-play-scraper\n",
            "Successfully installed google-play-scraper-1.2.7\n"
          ]
        }
      ],
      "source": [
        "pip install google-play-scraper pandas"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google_play_scraper import reviews, Sort\n",
        "import pandas as pd\n",
        "\n",
        "# Specify the App ID\n",
        "app_id = 'com.mercariapp.mercari'  # Replace this with your app's ID\n",
        "\n",
        "# Fetch reviews\n",
        "result, _ = reviews(\n",
        "    app_id,\n",
        "    lang='en',  # Language of the reviews\n",
        "    country='us',  # Country\n",
        "    sort=Sort.NEWEST,  # Sort by newest reviews\n",
        "    count=500  # Number of reviews to fetch\n",
        ")\n",
        "\n",
        "# Extract relevant fields\n",
        "reviews_data = []\n",
        "for r in result:\n",
        "    reviews_data.append({\n",
        "        'reviewId': r['reviewId'],\n",
        "        'userName': r['userName'],\n",
        "        'content': r['content'],\n",
        "        'score': r['score'],  # Rating given by the user\n",
        "        'thumbsUpCount': r['thumbsUpCount'],\n",
        "        'reviewCreatedVersion': r['reviewCreatedVersion'],\n",
        "        'at': r['at'].strftime('%Y-%m-%d %H:%M:%S')  # Timestamp of the review\n",
        "    })\n",
        "\n",
        "# Convert to DataFrame\n",
        "df = pd.DataFrame(reviews_data)\n",
        "\n",
        "# Save to CSV\n",
        "csv_filename = 'playstore_reviews.csv'\n",
        "df.to_csv(csv_filename, index=False)\n",
        "\n",
        "print(f\"Reviews have been saved to {csv_filename}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xmhTSKt-fGWT",
        "outputId": "2b4e195c-bbe9-4a40-bed1-033fcddd333c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reviews have been saved to playstore_reviews.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import plotly.express as px    #high level interface\n",
        "import plotly.graph_objects as go   #low level interface  graphical obj/"
      ],
      "metadata": {
        "id": "PfT8vmY6gLg-"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"/content/playstore_reviews.csv\")"
      ],
      "metadata": {
        "id": "hBOAZHvlgN99"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "HhfQCxV4hg-i",
        "outputId": "5831d26b-0191-44e0-90ae-c15c0379039c"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                               reviewId       userName  \\\n",
              "0  869e82b7-735e-4615-8518-8afb85b59c18           Tina   \n",
              "1  c9145045-c36b-4ce3-93fd-0fe7feba4e12          Katie   \n",
              "2  089ee544-512e-403d-a363-cd978ba5bc95  Julie Cassady   \n",
              "3  6e111a29-3429-43f2-85f9-099873b4b2b3    Emily Regan   \n",
              "4  be858b2d-fd95-4fe5-9537-a6abfd839fd0        Terry K   \n",
              "\n",
              "                                             content  score  thumbsUpCount  \\\n",
              "0  Love this site. I would rate it 5 stars as I h...      4              0   \n",
              "1  Fees are insane, I had 20 on my account went t...      1              1   \n",
              "2  order was received as expected in a timely man...      5              0   \n",
              "3  GREAT APP!! I love to explore all of the diffe...      5              0   \n",
              "4                                    Excellent buyer      5              0   \n",
              "\n",
              "  reviewCreatedVersion                   at  \n",
              "0               8.16.0  2024-11-11 03:05:25  \n",
              "1               8.24.1  2024-11-11 02:14:55  \n",
              "2               8.24.1  2024-11-11 00:11:16  \n",
              "3               8.24.1  2024-11-10 19:13:50  \n",
              "4               8.24.1  2024-11-10 19:04:03  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4722de9e-08a3-4a99-b3f9-1393f4c2be27\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>reviewId</th>\n",
              "      <th>userName</th>\n",
              "      <th>content</th>\n",
              "      <th>score</th>\n",
              "      <th>thumbsUpCount</th>\n",
              "      <th>reviewCreatedVersion</th>\n",
              "      <th>at</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>869e82b7-735e-4615-8518-8afb85b59c18</td>\n",
              "      <td>Tina</td>\n",
              "      <td>Love this site. I would rate it 5 stars as I h...</td>\n",
              "      <td>4</td>\n",
              "      <td>0</td>\n",
              "      <td>8.16.0</td>\n",
              "      <td>2024-11-11 03:05:25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>c9145045-c36b-4ce3-93fd-0fe7feba4e12</td>\n",
              "      <td>Katie</td>\n",
              "      <td>Fees are insane, I had 20 on my account went t...</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-11 02:14:55</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>089ee544-512e-403d-a363-cd978ba5bc95</td>\n",
              "      <td>Julie Cassady</td>\n",
              "      <td>order was received as expected in a timely man...</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-11 00:11:16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>6e111a29-3429-43f2-85f9-099873b4b2b3</td>\n",
              "      <td>Emily Regan</td>\n",
              "      <td>GREAT APP!! I love to explore all of the diffe...</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-10 19:13:50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>be858b2d-fd95-4fe5-9537-a6abfd839fd0</td>\n",
              "      <td>Terry K</td>\n",
              "      <td>Excellent buyer</td>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-10 19:04:03</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4722de9e-08a3-4a99-b3f9-1393f4c2be27')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-4722de9e-08a3-4a99-b3f9-1393f4c2be27 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-4722de9e-08a3-4a99-b3f9-1393f4c2be27');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-14c1a925-dce4-4e3d-bad4-6daa185d5d48\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-14c1a925-dce4-4e3d-bad4-6daa185d5d48')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-14c1a925-dce4-4e3d-bad4-6daa185d5d48 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 500,\n  \"fields\": [\n    {\n      \"column\": \"reviewId\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 500,\n        \"samples\": [\n          \"e06329ef-9253-4acf-a6c6-664bdc9f5f88\",\n          \"f4a3b38d-5fd9-488e-b4af-6a9eb733c68e\",\n          \"950512a2-ecdb-4204-816b-97587ecce198\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"userName\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 499,\n        \"samples\": [\n          \"Maryam Abubakar\",\n          \"Lynzi Edwards\",\n          \"Eric Thompson\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"content\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 491,\n        \"samples\": [\n          \"due to fees charged by Mercari, one can now expect go pay 1/3 to 1/2 more than the asking price.\",\n          \"Ever since Mercari started charging the buyer for all fees, my sales have gone down tremendously. They also allow buyers to get away with things without properly investigating and do not give the seller the benefit of the doubt. I am so disappointed in the current platform.\",\n          \"I'm very happy to be a part of Mecari . Great communication.. No complaints.\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"score\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 1,\n        \"max\": 5,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          1,\n          3,\n          5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"thumbsUpCount\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 16,\n        \"min\": 0,\n        \"max\": 265,\n        \"num_unique_values\": 23,\n        \"samples\": [\n          265,\n          29,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"reviewCreatedVersion\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 22,\n        \"samples\": [\n          \"8.16.0\",\n          \"7.82.0\",\n          \"8.9.0\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"at\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 500,\n        \"samples\": [\n          \"2024-10-25 08:10:20\",\n          \"2024-11-08 01:44:37\",\n          \"2024-10-24 14:38:46\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import warnings\n",
        "warnings.filterwarnings('ignore')"
      ],
      "metadata": {
        "id": "SbQXE7t5gUZM"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XxuPJvlQgVI8",
        "outputId": "9ab11427-24be-44c1-fa05-a57383e65c92"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['reviewId', 'userName', 'content', 'score', 'thumbsUpCount',\n",
              "       'reviewCreatedVersion', 'at'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.duplicated().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZoWrid0ZgZce",
        "outputId": "5b82188b-9627-46b0-8a8f-9312a57025bb"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "nuzeZpWCgcAr",
        "outputId": "45134d35-c11f-43a3-baf1-facc7b1fd453"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "reviewId                 0\n",
              "userName                 0\n",
              "content                  0\n",
              "score                    0\n",
              "thumbsUpCount            0\n",
              "reviewCreatedVersion    39\n",
              "at                       0\n",
              "dtype: int64"
            ],
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
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>reviewId</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>userName</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>content</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>score</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>thumbsUpCount</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>reviewCreatedVersion</th>\n",
              "      <td>39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>at</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(15,6))\n",
        "sns.countplot(x=df['score'], data = df, palette = 'hls')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "Kw5JrcPagjpQ",
        "outputId": "05a6dc9e-35e5-40e9-ff6b-c4096261150d"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1500x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABNYAAAINCAYAAADyXPJpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAn4klEQVR4nO3df5BV9X3/8dcCuhJllwGBhYioMYoYwB9Y3NFYBSqgpVp/JDpMikp1NGBrNkaHSfyVMSVxkmpjCZi0SjMjtYmpWk1FGQwQDaBgNWrQUUtHLCxQCayQ8EPZ7x+tO2789fXjLvcCj8fMmdl7zrnnvo8zx3GenntuTWtra2sAAAAAgI+lS6UHAAAAAIDdkbAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFOhW6QGqwc6dO7N69er06NEjNTU1lR4HAAAAgAppbW3Nm2++mQEDBqRLlw+/J01YS7J69eoMHDiw0mMAAAAAUCVWrVqVgw466EP3EdaS9OjRI8n//gOrq6ur8DQAAAAAVEpLS0sGDhzY1os+jLCWtH39s66uTlgDAAAA4P/rcWF+vAAAAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALdKj0AAAAA0LEeu3xZpUeATjdq1ohKj+CONQAAAAAoIawBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoEBFw9r06dNzwgknpEePHunbt2/OPvvsvPTSS+322bp1a6ZMmZLevXvngAMOyLnnnpu1a9e22+e1117LmWeemU996lPp27dvvva1r+Wtt97alacCAAAAwF6momFt4cKFmTJlSpYsWZJ58+Zlx44dOf3007Nly5a2fb7yla/kwQcfzE9/+tMsXLgwq1evzjnnnNO2/e23386ZZ56Z7du351e/+lX+6Z/+KbNnz871119fiVMCAAAAYC9R09ra2lrpId6xfv369O3bNwsXLswpp5ySTZs2pU+fPpkzZ07OO++8JMmLL76Yo446KosXL86JJ56Yhx9+OH/6p3+a1atXp1+/fkmSWbNm5dprr8369euz7777fuTntrS0pL6+Pps2bUpdXV2nniMAAAB0tscuX1bpEaDTjZo1olOO+3E6UVU9Y23Tpk1Jkl69eiVJli9fnh07dmTMmDFt+wwePDgHH3xwFi9enCRZvHhxhg4d2hbVkmTs2LFpaWnJCy+88L6fs23btrS0tLRbAAAAAODjqJqwtnPnzlx11VU56aST8rnPfS5J0tzcnH333Tc9e/Zst2+/fv3S3Nzcts+7o9o729/Z9n6mT5+e+vr6tmXgwIEdfDYAAAAA7OmqJqxNmTIlzz//fO65555O/6xp06Zl06ZNbcuqVas6/TMBAAAA2LN0q/QASTJ16tQ89NBDWbRoUQ466KC29Q0NDdm+fXs2btzY7q61tWvXpqGhoW2fJ598st3x3vnV0Hf2+UO1tbWpra3t4LMAAAAAYG9S0TvWWltbM3Xq1Nx333157LHHcuihh7bbfvzxx2efffbJ/Pnz29a99NJLee2119LY2JgkaWxszHPPPZd169a17TNv3rzU1dVlyJAhu+ZEAAAAANjrVPSOtSlTpmTOnDl54IEH0qNHj7ZnotXX16d79+6pr6/P5MmT09TUlF69eqWuri5XXnllGhsbc+KJJyZJTj/99AwZMiRf+tKXcsstt6S5uTnf+MY3MmXKFHelAQAAANBpKhrWZs6cmSQ59dRT262/6667ctFFFyVJbr311nTp0iXnnntutm3blrFjx+YHP/hB275du3bNQw89lCuuuCKNjY3Zf//9M2nSpHzzm9/cVacBAAAAwF6oprW1tbXSQ1RaS0tL6uvrs2nTptTV1VV6HAAAAPhEHrt8WaVHgE43ataITjnux+lEVfOroAAAAACwOxHWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUKBbpQfYGyz7q8srPQJ0uhHfn1XpEQAAAGCXcscaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKBARcPaokWLMmHChAwYMCA1NTW5//77222/6KKLUlNT024ZN25cu302bNiQiRMnpq6uLj179szkyZOzefPmXXgWAAAAAOyNKhrWtmzZkuHDh2fGjBkfuM+4ceOyZs2atuWf//mf222fOHFiXnjhhcybNy8PPfRQFi1alMsuu6yzRwcAAABgL9etkh8+fvz4jB8//kP3qa2tTUNDw/tuW7FiRebOnZunnnoqI0aMSJLcfvvtOeOMM/Ld7343AwYM6PCZAQAAACDZDZ6xtmDBgvTt2zdHHnlkrrjiirzxxhtt2xYvXpyePXu2RbUkGTNmTLp06ZKlS5d+4DG3bduWlpaWdgsAAAAAfBxVHdbGjRuXH//4x5k/f36+853vZOHChRk/fnzefvvtJElzc3P69u3b7j3dunVLr1690tzc/IHHnT59eurr69uWgQMHdup5AAAAALDnqehXQT/KBRdc0Pb30KFDM2zYsHzmM5/JggULMnr06OLjTps2LU1NTW2vW1paxDUAAAAAPpaqvmPtDx122GE58MAD88orryRJGhoasm7dunb7vPXWW9mwYcMHPpct+d/nttXV1bVbAAAAAODj2K3C2uuvv5433ngj/fv3T5I0NjZm48aNWb58eds+jz32WHbu3JmRI0dWakwAAAAA9gIV/Sro5s2b2+4+S5KVK1fmmWeeSa9evdKrV6/cdNNNOffcc9PQ0JBXX30111xzTQ4//PCMHTs2SXLUUUdl3LhxufTSSzNr1qzs2LEjU6dOzQUXXOAXQQEAAADoVBW9Y23ZsmU59thjc+yxxyZJmpqacuyxx+b6669P165d8+tf/zp/9md/liOOOCKTJ0/O8ccfn1/+8pepra1tO8bdd9+dwYMHZ/To0TnjjDNy8skn54c//GGlTgkAAACAvURF71g79dRT09ra+oHbH3nkkY88Rq9evTJnzpyOHAsAAAAAPtJu9Yw1AAAAAKgWwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUKAorI0aNSobN258z/qWlpaMGjXqk84EAAAAAFWvKKwtWLAg27dvf8/6rVu35pe//OUnHgoAAAAAql23j7Pzr3/967a/f/Ob36S5ubnt9dtvv525c+fm05/+dMdNBwAAAABV6mOFtWOOOSY1NTWpqal53698du/ePbfffnuHDQcAAAAA1epjhbWVK1emtbU1hx12WJ588sn06dOnbdu+++6bvn37pmvXrh0+JAAAAABUm48V1gYNGpQk2blzZ6cMAwAAAAC7i48V1t7t5Zdfzi9+8YusW7fuPaHt+uuv/8SDAQAAAEA1KwprP/rRj3LFFVfkwAMPTENDQ2pqatq21dTUCGsAAAAA7PGKwtrNN9+cb33rW7n22ms7eh4AAAAA2C10KXnTb3/725x//vkdPQsAAAAA7DaKwtr555+fRx99tKNnAQAAAIDdRtFXQQ8//PBcd911WbJkSYYOHZp99tmn3fa/+qu/6pDhAAAAAKBaFYW1H/7whznggAOycOHCLFy4sN22mpoaYQ0AAACAPV5RWFu5cmVHzwEAAAAAu5WiZ6wBAAAAwN6u6I61Sy655EO333nnnUXDAAAAAMDuoiis/fa3v233eseOHXn++eezcePGjBo1qkMGAwAAAIBqVhTW7rvvvves27lzZ6644op85jOf+cRDAQAAAEC167BnrHXp0iVNTU259dZbO+qQAAAAAFC1OvTHC1599dW89dZbHXlIAAAAAKhKRV8FbWpqave6tbU1a9asyc9//vNMmjSpQwYDAAAAgGpWFNb+4z/+o93rLl26pE+fPvne9773kb8YCgAAAAB7gqKw9otf/KKj5wAAAACA3UpRWHvH+vXr89JLLyVJjjzyyPTp06dDhgIAAACAalf04wVbtmzJJZdckv79++eUU07JKaeckgEDBmTy5Mn53e9+19EzAgAAAEDVKQprTU1NWbhwYR588MFs3LgxGzduzAMPPJCFCxfmq1/9akfPCAAAAABVp+iroD/72c9y77335tRTT21bd8YZZ6R79+75whe+kJkzZ3bUfAAAAABQlYruWPvd736Xfv36vWd93759fRUUAAAAgL1CUVhrbGzMDTfckK1bt7at+/3vf5+bbropjY2NHTYcAAAAAFSroq+C3nbbbRk3blwOOuigDB8+PEny7LPPpra2No8++miHDggAAAAA1agorA0dOjQvv/xy7r777rz44otJkgsvvDATJ05M9+7dO3RAAAAAAKhGRWFt+vTp6devXy699NJ26++8886sX78+1157bYcMBwAAAADVqugZa3fccUcGDx78nvVHH310Zs2a9YmHAgAAAIBqVxTWmpub079///es79OnT9asWfOJhwIAAACAalcU1gYOHJgnnnjiPeufeOKJDBgw4BMPBQAAAADVrugZa5deemmuuuqq7NixI6NGjUqSzJ8/P9dcc02++tWvduiAAAAAAFCNisLa1772tbzxxhv58pe/nO3btydJ9ttvv1x77bWZNm1ahw4IAAAAANWoKKzV1NTkO9/5Tq677rqsWLEi3bt3z2c/+9nU1tZ29HwAAAAAUJWKwto7DjjggJxwwgkdNQsAAAAA7DaKfrwAAAAAAPZ2whoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACgQEXD2qJFizJhwoQMGDAgNTU1uf/++9ttb21tzfXXX5/+/fune/fuGTNmTF5++eV2+2zYsCETJ05MXV1devbsmcmTJ2fz5s278CwAAAAA2BtVNKxt2bIlw4cPz4wZM953+y233JLvf//7mTVrVpYuXZr9998/Y8eOzdatW9v2mThxYl544YXMmzcvDz30UBYtWpTLLrtsV50CAAAAAHupbpX88PHjx2f8+PHvu621tTW33XZbvvGNb+Sss85Kkvz4xz9Ov379cv/99+eCCy7IihUrMnfu3Dz11FMZMWJEkuT222/PGWecke9+97sZMGDALjsXAAAAAPYuVfuMtZUrV6a5uTljxoxpW1dfX5+RI0dm8eLFSZLFixenZ8+ebVEtScaMGZMuXbpk6dKlH3jsbdu2paWlpd0CAAAAAB9H1Ya15ubmJEm/fv3are/Xr1/btubm5vTt27fd9m7duqVXr15t+7yf6dOnp76+vm0ZOHBgB08PAAAAwJ6uasNaZ5o2bVo2bdrUtqxatarSIwEAAACwm6nasNbQ0JAkWbt2bbv1a9eubdvW0NCQdevWtdv+1ltvZcOGDW37vJ/a2trU1dW1WwAAAADg46jasHbooYemoaEh8+fPb1vX0tKSpUuXprGxMUnS2NiYjRs3Zvny5W37PPbYY9m5c2dGjhy5y2cGAAAAYO9R0V8F3bx5c1555ZW21ytXrswzzzyTXr165eCDD85VV12Vm2++OZ/97Gdz6KGH5rrrrsuAAQNy9tlnJ0mOOuqojBs3LpdeemlmzZqVHTt2ZOrUqbngggv8IigAAAAAnaqiYW3ZsmU57bTT2l43NTUlSSZNmpTZs2fnmmuuyZYtW3LZZZdl48aNOfnkkzN37tzst99+be+5++67M3Xq1IwePTpdunTJueeem+9///u7/FwAAAAA2LtUNKydeuqpaW1t/cDtNTU1+eY3v5lvfvObH7hPr169MmfOnM4YDwAAAAA+UNU+Yw0AAAAAqpmwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWqOqzdeOONqampabcMHjy4bfvWrVszZcqU9O7dOwcccEDOPffcrF27toITAwAAALC3qOqwliRHH3101qxZ07Y8/vjjbdu+8pWv5MEHH8xPf/rTLFy4MKtXr84555xTwWkBAAAA2Ft0q/QAH6Vbt25paGh4z/pNmzblH//xHzNnzpyMGjUqSXLXXXflqKOOypIlS3LiiSfu6lEBAAAA2ItU/R1rL7/8cgYMGJDDDjssEydOzGuvvZYkWb58eXbs2JExY8a07Tt48OAcfPDBWbx48Ycec9u2bWlpaWm3AAAAAMDHUdVhbeTIkZk9e3bmzp2bmTNnZuXKlfn85z+fN998M83Nzdl3333Ts2fPdu/p169fmpubP/S406dPT319fdsycODATjwLAAAAAPZEVf1V0PHjx7f9PWzYsIwcOTKDBg3KT37yk3Tv3r34uNOmTUtTU1Pb65aWFnENAAAAgI+lqu9Y+0M9e/bMEUcckVdeeSUNDQ3Zvn17Nm7c2G6ftWvXvu8z2d6ttrY2dXV17RYAAAAA+Dh2q7C2efPmvPrqq+nfv3+OP/747LPPPpk/f37b9pdeeimvvfZaGhsbKzglAAAAAHuDqv4q6NVXX50JEyZk0KBBWb16dW644YZ07do1F154Yerr6zN58uQ0NTWlV69eqaury5VXXpnGxka/CAoAAABAp6vqsPb666/nwgsvzBtvvJE+ffrk5JNPzpIlS9KnT58kya233pouXbrk3HPPzbZt2zJ27Nj84Ac/qPDUAAAAAOwNqjqs3XPPPR+6fb/99suMGTMyY8aMXTQRAAAAAPyv3eoZawAAAABQLYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABToVukBACrp35ZdXukRoNP92YhZlR4BAAD2SO5YAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFulV6AACAD3L5sh9UegTodLNGfLnSIwAAhdyxBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIAC3So9AAAAsPu5/JZllR4BOt2sa0ZUegSgyrljDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAFhDUAAAAAKCCsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAAAAQAFhDQAAAAAKCGsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAUENYAAAAAoICwBgAAAAAF9piwNmPGjBxyyCHZb7/9MnLkyDz55JOVHgkAAACAPdgeEdb+5V/+JU1NTbnhhhvy9NNPZ/jw4Rk7dmzWrVtX6dEAAAAA2EPtEWHtb//2b3PppZfm4osvzpAhQzJr1qx86lOfyp133lnp0QAAAADYQ3Wr9ACf1Pbt27N8+fJMmzatbV2XLl0yZsyYLF68+H3fs23btmzbtq3t9aZNm5IkLS0tnTLj5u3bO+W4UE066/rpbL/b7Ppkz7e7Xp9Jsn3z7ys9AnS63fUa3b51c6VHgE63u16fSbJlu2uUPV9nXaPvHLe1tfUj993tw9r//M//5O23306/fv3are/Xr19efPHF933P9OnTc9NNN71n/cCBAztlRtgr3HFXpScAPpDrE6rZXbm60iMAH+CuGyo9AfChOvk/c998883U19d/6D67fVgrMW3atDQ1NbW93rlzZzZs2JDevXunpqamgpPREVpaWjJw4MCsWrUqdXV1lR4HeBfXJ1Q31yhUL9cnVDfX6J6ltbU1b775ZgYMGPCR++72Ye3AAw9M165ds3bt2nbr165dm4aGhvd9T21tbWpra9ut69mzZ2eNSIXU1dX5FxpUKdcnVDfXKFQv1ydUN9fonuOj7lR7x27/4wX77rtvjj/++MyfP79t3c6dOzN//vw0NjZWcDIAAAAA9mS7/R1rSdLU1JRJkyZlxIgR+aM/+qPcdttt2bJlSy6++OJKjwYAAADAHmqPCGtf/OIXs379+lx//fVpbm7OMccck7lz577nBw3YO9TW1uaGG254z9d9gcpzfUJ1c41C9XJ9QnVzje69alr/f347FAAAAABoZ7d/xhoAAAAAVIKwBgAAAAAFhDUAAAAAKCCsAQAAAEABYY09xqJFizJhwoQMGDAgNTU1uf/++ys9EvB/pk+fnhNOOCE9evRI3759c/bZZ+ell16q9FjA/5k5c2aGDRuWurq61NXVpbGxMQ8//HClxwLex7e//e3U1NTkqquuqvQoQJIbb7wxNTU17ZbBgwdXeix2IWGNPcaWLVsyfPjwzJgxo9KjAH9g4cKFmTJlSpYsWZJ58+Zlx44dOf3007Nly5ZKjwYkOeigg/Ltb387y5cvz7JlyzJq1KicddZZeeGFFyo9GvAuTz31VO64444MGzas0qMA73L00UdnzZo1bcvjjz9e6ZHYhbpVegDoKOPHj8/48eMrPQbwPubOndvu9ezZs9O3b98sX748p5xySoWmAt4xYcKEdq+/9a1vZebMmVmyZEmOPvroCk0FvNvmzZszceLE/OhHP8rNN99c6XGAd+nWrVsaGhoqPQYV4o41AHa5TZs2JUl69epV4UmAP/T222/nnnvuyZYtW9LY2FjpcYD/M2XKlJx55pkZM2ZMpUcB/sDLL7+cAQMG5LDDDsvEiRPz2muvVXokdiF3rAGwS+3cuTNXXXVVTjrppHzuc5+r9DjA/3nuuefS2NiYrVu35oADDsh9992XIUOGVHosIMk999yTp59+Ok899VSlRwH+wMiRIzN79uwceeSRWbNmTW666aZ8/vOfz/PPP58ePXpUejx2AWENgF1qypQpef755z17AqrMkUcemWeeeSabNm3Kvffem0mTJmXhwoXiGlTYqlWr8td//deZN29e9ttvv0qPA/yBdz+OaNiwYRk5cmQGDRqUn/zkJ5k8eXIFJ2NXEdYA2GWmTp2ahx56KIsWLcpBBx1U6XGAd9l3331z+OGHJ0mOP/74PPXUU/m7v/u73HHHHRWeDPZuy5cvz7p163Lccce1rXv77bezaNGi/P3f/322bduWrl27VnBC4N169uyZI444Iq+88kqlR2EXEdYA6HStra258sorc99992XBggU59NBDKz0S8BF27tyZbdu2VXoM2OuNHj06zz33XLt1F198cQYPHpxrr71WVIMqs3nz5rz66qv50pe+VOlR2EWENfYYmzdvbvd/BVauXJlnnnkmvXr1ysEHH1zByYApU6Zkzpw5eeCBB9KjR480NzcnSerr69O9e/cKTwdMmzYt48ePz8EHH5w333wzc+bMyYIFC/LII49UejTY6/Xo0eM9zyTdf//907t3b88qhSpw9dVXZ8KECRk0aFBWr16dG264IV27ds2FF15Y6dHYRYQ19hjLli3Laaed1va6qakpSTJp0qTMnj27QlMBSTJz5swkyamnntpu/V133ZWLLrpo1w8EtLNu3br8xV/8RdasWZP6+voMGzYsjzzySP7kT/6k0qMBQFV7/fXXc+GFF+aNN95Inz59cvLJJ2fJkiXp06dPpUdjF6lpbW1trfQQAAAAALC76VLpAQAAAABgdySsAQAAAEABYQ0AAAAACghrAAAAAFBAWAMAAACAAsIaAAAAABQQ1gAAAACggLAGAAAAAAWENQAAAAAoIKwBAPCxbN++vdIjAABUBWENAGAPce+992bo0KHp3r17evfunTFjxmTLli1JkjvvvDNHH310amtr079//0ydOrXtfa+99lrOOuusHHDAAamrq8sXvvCFrF27tm37jTfemGOOOSb/8A//kEMPPTT77bdfkmTjxo35y7/8y/Tp0yd1dXUZNWpUnn322V170gAAFSSsAQDsAdasWZMLL7wwl1xySVasWJEFCxbknHPOSWtra2bOnJkpU6bksssuy3PPPZd/+7d/y+GHH54k2blzZ84666xs2LAhCxcuzLx58/Kf//mf+eIXv9ju+K+88kp+9rOf5V//9V/zzDPPJEnOP//8rFu3Lg8//HCWL1+e4447LqNHj86GDRt29ekDAFRETWtra2ulhwAA4JN5+umnc/zxx+e//uu/MmjQoHbbPv3pT+fiiy/OzTff/J73zZs3L+PHj8/KlSszcODAJMlvfvObHH300XnyySdzwgkn5MYbb8zf/M3f5L//+7/Tp0+fJMnjjz+eM888M+vWrUttbW3b8Q4//PBcc801ueyyyzrxbAEAqkO3Sg8AAMAnN3z48IwePTpDhw7N2LFjc/rpp+e8887Ljh07snr16owePfp937dixYoMHDiwLaolyZAhQ9KzZ8+sWLEiJ5xwQpJk0KBBbVEtSZ599tls3rw5vXv3bne83//+93n11Vc74QwBAKqPsAYAsAfo2rVr5s2bl1/96ld59NFHc/vtt+frX/965s+f3yHH33///du93rx5c/r3758FCxa8Z9+ePXt2yGcCAFQ7YQ0AYA9RU1OTk046KSeddFKuv/76DBo0KPPmzcshhxyS+fPn57TTTnvPe4466qisWrUqq1atavdV0I0bN2bIkCEf+FnHHXdcmpub061btxxyyCGddUoAAFVNWAMA2AMsXbo08+fPz+mnn56+fftm6dKlWb9+fY466qjceOONufzyy9O3b9+MHz8+b775Zp544olceeWVGTNmTIYOHZqJEyfmtttuy1tvvZUvf/nL+eM//uOMGDHiAz9vzJgxaWxszNlnn51bbrklRxxxRFavXp2f//zn+fM///MPfS8AwJ5CWAMA2APU1dVl0aJFue2229LS0pJBgwble9/7XsaPH58k2bp1a2699dZcffXVOfDAA3Peeecl+d+73B544IFceeWVOeWUU9KlS5eMGzcut99++4d+Xk1NTf793/89X//613PxxRdn/fr1aWhoyCmnnJJ+/fp1+vkCAFQDvwoKAAAAAAW6VHoAAAAAANgdCWsAAAAAUEBYAwAAAIACwhoAAAAAFBDWAAAAAKCAsAYAAAAABYQ1AAAAACggrAEAAABAAWENAAAAAAoIawAAAABQQFgDAAAAgALCGgAAAAAU+H/Tzd1ZZuN/xAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['at'] = pd.to_datetime(df['at'])"
      ],
      "metadata": {
        "id": "665Vxddfhu3i"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['at']"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "SUgQMzQehyxX",
        "outputId": "2172f164-61ee-40fd-ea9d-824dd2543ba4"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0     2024-11-11 03:05:25\n",
              "1     2024-11-11 02:14:55\n",
              "2     2024-11-11 00:11:16\n",
              "3     2024-11-10 19:13:50\n",
              "4     2024-11-10 19:04:03\n",
              "              ...        \n",
              "495   2024-10-18 19:28:20\n",
              "496   2024-10-18 17:45:12\n",
              "497   2024-10-18 16:37:01\n",
              "498   2024-10-18 14:54:04\n",
              "499   2024-10-18 14:12:20\n",
              "Name: at, Length: 500, dtype: datetime64[ns]"
            ],
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
              "      <th>at</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2024-11-11 03:05:25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2024-11-11 02:14:55</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2024-11-11 00:11:16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2024-11-10 19:13:50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2024-11-10 19:04:03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>2024-10-18 19:28:20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>2024-10-18 17:45:12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>2024-10-18 16:37:01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>2024-10-18 14:54:04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>2024-10-18 14:12:20</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 1 columns</p>\n",
              "</div><br><label><b>dtype:</b> datetime64[ns]</label>"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df1 = df.copy()"
      ],
      "metadata": {
        "id": "wCIyCgfph1vv"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df1.set_index('at',inplace=True)"
      ],
      "metadata": {
        "id": "GpX8f6Zkh4W4"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "start_date = df1.index.min()\n",
        "end_date = df1.index.max()"
      ],
      "metadata": {
        "id": "enTluS1Gh7ml"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"start date: \",start_date)\n",
        "print(\"end date: \",end_date)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BQQgyNjoh-_D",
        "outputId": "144ec9a4-1c08-436e-ee4a-b729b74db579"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "start date:  2024-10-18 14:12:20\n",
            "end date:  2024-11-11 03:05:25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "week_delta = pd.Timedelta(days=6)\n",
        "current_date = start_date"
      ],
      "metadata": {
        "id": "ZXaZwnVsiDtZ"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "while current_date<=end_date:\n",
        "  start_week = current_date\n",
        "  print(start_week)\n",
        "  end_week = current_date + week_delta\n",
        "  print(end_week)\n",
        "  current_week_data = df1[(df1.index >= start_week) & (df1.index < end_week)]\n",
        "  print(current_week_data)\n",
        "  weekly_counts = current_week_data.resample('D').size()   #stats of a particular day {D}\n",
        "  print(weekly_counts)\n",
        "  fig = px.bar(weekly_counts, x=weekly_counts.index, y=weekly_counts.values,\n",
        "                 labels={'x': 'Date', 'y': 'Number of Reviews'},\n",
        "                 title=f'Reviews for Week {start_week.strftime(\"%Y-%m-%d\")} to {end_week.strftime(\"%Y-%m-%d\")}')\n",
        "  fig.update_layout(xaxis_tickangle=-45)\n",
        "  fig.show()\n",
        "  current_date += week_delta"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "YBJscjYwiIm3",
        "outputId": "43664979-8888-487a-bc3a-3a471816c5d1"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-10-18 14:12:20\n",
            "2024-10-24 14:12:20\n",
            "                                                 reviewId           userName  \\\n",
            "at                                                                             \n",
            "2024-10-24 13:46:14  7eaf67b7-b877-4996-b50b-2ca74100ea64              Diane   \n",
            "2024-10-24 07:54:43  e3ccbfc2-09bf-4b90-a805-590c98552939            Sarah C   \n",
            "2024-10-24 04:57:20  0fdc28e2-9ac8-404b-bb19-ab12ee3fb2b6  Demecio Vigil Jr.   \n",
            "2024-10-24 03:24:49  55efa282-5a52-443e-9dd3-c84b667a24ac            Angel A   \n",
            "2024-10-24 01:08:44  593dd057-74c0-4ea3-a896-b6936afc86ee       Rachel Leigh   \n",
            "...                                                   ...                ...   \n",
            "2024-10-18 19:28:20  015c06c5-e208-4dd0-9c66-245f36f5aa48     Keithen Booher   \n",
            "2024-10-18 17:45:12  be8a0554-a37d-46d5-8504-24a15d879233           wolf07ga   \n",
            "2024-10-18 16:37:01  7958eca8-72c9-48ef-9b6c-d7226447f88a     Nick Guzman G.   \n",
            "2024-10-18 14:54:04  10a2b3b3-a420-4ba0-a748-0660e3ed677d       Vampiric Fae   \n",
            "2024-10-18 14:12:20  47112154-0f61-4a79-bfa6-97667cd6993e                Bob   \n",
            "\n",
            "                                                               content  score  \\\n",
            "at                                                                              \n",
            "2024-10-24 13:46:14  Poor customer service. I will update if they e...      1   \n",
            "2024-10-24 07:54:43               All the best things and for a deal!!      5   \n",
            "2024-10-24 04:57:20  Thank you Jesus and God bless you 🙏❤️‍🔥☪️☮️☦️☯...      5   \n",
            "2024-10-24 03:24:49  Update: ADD the feature to send PICTURES. The ...      1   \n",
            "2024-10-24 01:08:44  I have used this app for 6 years to buy and se...      1   \n",
            "...                                                                ...    ...   \n",
            "2024-10-18 19:28:20                                 great shopping app      5   \n",
            "2024-10-18 17:45:12  Fantastic place to shop that gives competition...      5   \n",
            "2024-10-18 16:37:01  They used to be Good Now they charge you a ser...      1   \n",
            "2024-10-18 14:54:04  PLEASE GET RID OF THE GENERAL MESSAGING FEATUR...      3   \n",
            "2024-10-18 14:12:20  I will not be using this app or platform again...      1   \n",
            "\n",
            "                     thumbsUpCount reviewCreatedVersion  \n",
            "at                                                       \n",
            "2024-10-24 13:46:14              4               8.23.0  \n",
            "2024-10-24 07:54:43              0               8.23.0  \n",
            "2024-10-24 04:57:20              0               8.23.0  \n",
            "2024-10-24 03:24:49             23               8.23.0  \n",
            "2024-10-24 01:08:44              0                  NaN  \n",
            "...                            ...                  ...  \n",
            "2024-10-18 19:28:20              0               8.23.0  \n",
            "2024-10-18 17:45:12              0               8.23.0  \n",
            "2024-10-18 16:37:01              0               8.23.0  \n",
            "2024-10-18 14:54:04              3               8.22.0  \n",
            "2024-10-18 14:12:20             18               8.22.0  \n",
            "\n",
            "[124 rows x 6 columns]\n",
            "at\n",
            "2024-10-18     9\n",
            "2024-10-19    16\n",
            "2024-10-20    17\n",
            "2024-10-21    25\n",
            "2024-10-22    27\n",
            "2024-10-23    24\n",
            "2024-10-24     6\n",
            "Freq: D, dtype: int64\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"c3b50b4b-4fd2-4c14-a73f-e37424863153\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"c3b50b4b-4fd2-4c14-a73f-e37424863153\")) {                    Plotly.newPlot(                        \"c3b50b4b-4fd2-4c14-a73f-e37424863153\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"at=%{x}\\u003cbr\\u003eNumber of Reviews=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\"],\"xaxis\":\"x\",\"y\":[9,16,17,25,27,24,6],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"at\"},\"tickangle\":-45},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Number of Reviews\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Reviews for Week 2024-10-18 to 2024-10-24\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('c3b50b4b-4fd2-4c14-a73f-e37424863153');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-10-24 14:12:20\n",
            "2024-10-30 14:12:20\n",
            "                                                 reviewId         userName  \\\n",
            "at                                                                           \n",
            "2024-10-30 14:00:05  1f1755df-fc3c-4b88-bccf-b33d62e96970     Belle Cooper   \n",
            "2024-10-30 13:34:51  e1e11be4-10b8-4bb3-9b6d-66edfd96a310  Janille Maclean   \n",
            "2024-10-30 11:52:41  5b776b6f-d624-42da-954e-97e7dbf5d775     Mario Galvez   \n",
            "2024-10-30 08:27:12  b586f02b-00b4-4c99-ae8f-805b781a0794     Angela Leger   \n",
            "2024-10-30 02:02:36  903dac49-466f-4f12-813b-281c771c93d3           Randal   \n",
            "...                                                   ...              ...   \n",
            "2024-10-24 17:16:12  8f90bb29-dd7c-49e3-8d79-9784824deecc     Mike Carroll   \n",
            "2024-10-24 16:32:43  65b68639-a6ad-4f5a-8d4b-de8f6068979f      Alex Belone   \n",
            "2024-10-24 15:10:13  73371b85-e603-4239-913d-80ad4088165d      Summer Hall   \n",
            "2024-10-24 14:38:46  950512a2-ecdb-4204-816b-97587ecce198     David Devine   \n",
            "2024-10-24 14:15:40  1182f2c9-c1a8-4436-870e-f89002786e44       Jeff Jones   \n",
            "\n",
            "                                                               content  score  \\\n",
            "at                                                                              \n",
            "2024-10-30 14:00:05      Too many hoops to get through for assistance!      2   \n",
            "2024-10-30 13:34:51  Reduced my rating from 5 star to 2 star. They ...      2   \n",
            "2024-10-30 11:52:41  Fees are way to high from purchasing items whi...      2   \n",
            "2024-10-30 08:27:12                           New items, great prices!      5   \n",
            "2024-10-30 02:02:36                                       awesome site      5   \n",
            "...                                                                ...    ...   \n",
            "2024-10-24 17:16:12                                   great experience      5   \n",
            "2024-10-24 16:32:43  Having to pay more to buy stuff doesn't really...      1   \n",
            "2024-10-24 15:10:13  What is up with all these \"payment processing ...      1   \n",
            "2024-10-24 14:38:46  Charging buyers selling fees and not doing any...      1   \n",
            "2024-10-24 14:15:40  App is easy and works well! I highly recommend...      5   \n",
            "\n",
            "                     thumbsUpCount reviewCreatedVersion  \n",
            "at                                                       \n",
            "2024-10-30 14:00:05              0                  NaN  \n",
            "2024-10-30 13:34:51              0               8.23.0  \n",
            "2024-10-30 11:52:41              0               8.23.0  \n",
            "2024-10-30 08:27:12              0               8.23.0  \n",
            "2024-10-30 02:02:36              0               8.23.0  \n",
            "...                            ...                  ...  \n",
            "2024-10-24 17:16:12              0               8.23.0  \n",
            "2024-10-24 16:32:43              6               8.23.0  \n",
            "2024-10-24 15:10:13              0                  NaN  \n",
            "2024-10-24 14:38:46              0               8.23.0  \n",
            "2024-10-24 14:15:40              1               8.23.0  \n",
            "\n",
            "[120 rows x 6 columns]\n",
            "at\n",
            "2024-10-24    10\n",
            "2024-10-25    15\n",
            "2024-10-26    21\n",
            "2024-10-27    26\n",
            "2024-10-28    22\n",
            "2024-10-29    20\n",
            "2024-10-30     6\n",
            "Freq: D, dtype: int64\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"140fd587-af19-4779-9a12-508f7d992a5b\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"140fd587-af19-4779-9a12-508f7d992a5b\")) {                    Plotly.newPlot(                        \"140fd587-af19-4779-9a12-508f7d992a5b\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"at=%{x}\\u003cbr\\u003eNumber of Reviews=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\"],\"xaxis\":\"x\",\"y\":[10,15,21,26,22,20,6],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"at\"},\"tickangle\":-45},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Number of Reviews\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Reviews for Week 2024-10-24 to 2024-10-30\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('140fd587-af19-4779-9a12-508f7d992a5b');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-10-30 14:12:20\n",
            "2024-11-05 14:12:20\n",
            "                                                 reviewId  \\\n",
            "at                                                          \n",
            "2024-11-05 11:49:38  de8830a5-2dbf-48da-813d-e68348a6765e   \n",
            "2024-11-05 07:28:11  f97a565c-73bc-4177-9733-b7055bea5aa9   \n",
            "2024-11-05 05:33:33  1421903f-f355-416c-9f52-10f2e6f2affa   \n",
            "2024-11-05 03:46:46  c1f50a88-c3c8-43c1-92ef-54cc3de6dd63   \n",
            "2024-11-05 01:13:47  4df10264-9121-4a75-b9b8-3b9740e9efdd   \n",
            "...                                                   ...   \n",
            "2024-10-30 19:57:06  1069547c-fd24-4f00-b5d1-011563623f89   \n",
            "2024-10-30 18:32:27  b78f80e4-6fcd-4461-b792-ffd5010f329d   \n",
            "2024-10-30 17:19:18  13b20619-677c-4252-89a1-c9a9a6d3234e   \n",
            "2024-10-30 16:35:36  57409fc0-4a52-4258-8c22-d5d65c9b30e5   \n",
            "2024-10-30 14:33:40  159421d5-bb9e-42d0-88c9-02e3b8e8b6de   \n",
            "\n",
            "                                userName  \\\n",
            "at                                         \n",
            "2024-11-05 11:49:38  Kimberly Thibodeaux   \n",
            "2024-11-05 07:28:11                  JAY   \n",
            "2024-11-05 05:33:33       Cynthia Lohnes   \n",
            "2024-11-05 03:46:46      Nicholas Foshee   \n",
            "2024-11-05 01:13:47           Elin Hayes   \n",
            "...                                  ...   \n",
            "2024-10-30 19:57:06          Donald Rull   \n",
            "2024-10-30 18:32:27         John T Gream   \n",
            "2024-10-30 17:19:18           Lybni Cruz   \n",
            "2024-10-30 16:35:36          Tracy Nosal   \n",
            "2024-10-30 14:33:40                  SRS   \n",
            "\n",
            "                                                               content  score  \\\n",
            "at                                                                              \n",
            "2024-11-05 11:49:38  This App was great until it's time for help. I...      3   \n",
            "2024-11-05 07:28:11  Was good but my account has been closed and fr...      1   \n",
            "2024-11-05 05:33:33  Please bring back the ability to sort by color...      2   \n",
            "2024-11-05 03:46:46                                       Great store.      5   \n",
            "2024-11-05 01:13:47  Not user friendly when there's an issue. Nearl...      1   \n",
            "...                                                                ...    ...   \n",
            "2024-10-30 19:57:06  Unfortunately, as a buyer I've learned that Me...      1   \n",
            "2024-10-30 18:32:27  so far mercari is looking good I hope to purch...      5   \n",
            "2024-10-30 17:19:18  I love that the mErcari staff are so on point ...      5   \n",
            "2024-10-30 16:35:36  I love the merchandise. Shipping takes a littl...      5   \n",
            "2024-10-30 14:33:40  \"SCAM ALERT - AVOID THIS APP!\" This app is an ...      1   \n",
            "\n",
            "                     thumbsUpCount reviewCreatedVersion  \n",
            "at                                                       \n",
            "2024-11-05 11:49:38              0               8.24.1  \n",
            "2024-11-05 07:28:11              2               8.24.1  \n",
            "2024-11-05 05:33:33              6               8.24.1  \n",
            "2024-11-05 03:46:46              0               8.24.1  \n",
            "2024-11-05 01:13:47              2               8.24.1  \n",
            "...                            ...                  ...  \n",
            "2024-10-30 19:57:06              3               8.23.0  \n",
            "2024-10-30 18:32:27              0               8.23.0  \n",
            "2024-10-30 17:19:18              0               8.23.0  \n",
            "2024-10-30 16:35:36              0               8.23.0  \n",
            "2024-10-30 14:33:40              0               8.23.0  \n",
            "\n",
            "[119 rows x 6 columns]\n",
            "at\n",
            "2024-10-30    12\n",
            "2024-10-31    22\n",
            "2024-11-01    26\n",
            "2024-11-02    20\n",
            "2024-11-03    16\n",
            "2024-11-04    12\n",
            "2024-11-05    11\n",
            "Freq: D, dtype: int64\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"8590cccf-e3fa-4de3-9489-b06de859b50c\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"8590cccf-e3fa-4de3-9489-b06de859b50c\")) {                    Plotly.newPlot(                        \"8590cccf-e3fa-4de3-9489-b06de859b50c\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"at=%{x}\\u003cbr\\u003eNumber of Reviews=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\"],\"xaxis\":\"x\",\"y\":[12,22,26,20,16,12,11],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"at\"},\"tickangle\":-45},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Number of Reviews\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Reviews for Week 2024-10-30 to 2024-11-05\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('8590cccf-e3fa-4de3-9489-b06de859b50c');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-11-05 14:12:20\n",
            "2024-11-11 14:12:20\n",
            "                                                 reviewId          userName  \\\n",
            "at                                                                            \n",
            "2024-11-11 03:05:25  869e82b7-735e-4615-8518-8afb85b59c18              Tina   \n",
            "2024-11-11 02:14:55  c9145045-c36b-4ce3-93fd-0fe7feba4e12             Katie   \n",
            "2024-11-11 00:11:16  089ee544-512e-403d-a363-cd978ba5bc95     Julie Cassady   \n",
            "2024-11-10 19:13:50  6e111a29-3429-43f2-85f9-099873b4b2b3       Emily Regan   \n",
            "2024-11-10 19:04:03  be858b2d-fd95-4fe5-9537-a6abfd839fd0           Terry K   \n",
            "...                                                   ...               ...   \n",
            "2024-11-05 18:09:27  33311d23-e148-4f93-bf06-169b2157068c    Dorian Fortner   \n",
            "2024-11-05 17:27:33  29446460-121e-418f-9845-1fc7153ab790      Steven Bucks   \n",
            "2024-11-05 16:19:47  8bafe1ef-f2f8-4a71-96ec-1a94e258c706           weesnaw   \n",
            "2024-11-05 16:12:13  f486ffa8-aaa3-462c-b960-81160a2757ca  Samuel Abernathy   \n",
            "2024-11-05 15:55:23  aea12322-ca0f-46a1-b8a0-6773a90eebbd              C NR   \n",
            "\n",
            "                                                               content  score  \\\n",
            "at                                                                              \n",
            "2024-11-11 03:05:25  Love this site. I would rate it 5 stars as I h...      4   \n",
            "2024-11-11 02:14:55  Fees are insane, I had 20 on my account went t...      1   \n",
            "2024-11-11 00:11:16  order was received as expected in a timely man...      5   \n",
            "2024-11-10 19:13:50  GREAT APP!! I love to explore all of the diffe...      5   \n",
            "2024-11-10 19:04:03                                    Excellent buyer      5   \n",
            "...                                                                ...    ...   \n",
            "2024-11-05 18:09:27  Yeah. Mercari lost me when they added them fee...      1   \n",
            "2024-11-05 17:27:33  I don't think it's fair that they put fees as ...      3   \n",
            "2024-11-05 16:19:47  Used to be normal. Now it just adds 100 dollar...      2   \n",
            "2024-11-05 16:12:13  The customer service sucks. I've waited for 2 ...      1   \n",
            "2024-11-05 15:55:23  I've been using this app forever and lately I'...      5   \n",
            "\n",
            "                     thumbsUpCount reviewCreatedVersion  \n",
            "at                                                       \n",
            "2024-11-11 03:05:25              0               8.16.0  \n",
            "2024-11-11 02:14:55              1               8.24.1  \n",
            "2024-11-11 00:11:16              0               8.24.1  \n",
            "2024-11-10 19:13:50              0               8.24.1  \n",
            "2024-11-10 19:04:03              0               8.24.1  \n",
            "...                            ...                  ...  \n",
            "2024-11-05 18:09:27              1               8.20.0  \n",
            "2024-11-05 17:27:33              0               8.24.1  \n",
            "2024-11-05 16:19:47              1               8.24.1  \n",
            "2024-11-05 16:12:13              1                  NaN  \n",
            "2024-11-05 15:55:23              0               8.24.1  \n",
            "\n",
            "[137 rows x 6 columns]\n",
            "at\n",
            "2024-11-05    15\n",
            "2024-11-06    14\n",
            "2024-11-07    32\n",
            "2024-11-08    28\n",
            "2024-11-09    31\n",
            "2024-11-10    14\n",
            "2024-11-11     3\n",
            "Freq: D, dtype: int64\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"ea235245-9d5e-474b-9e4d-591f69c124e9\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"ea235245-9d5e-474b-9e4d-591f69c124e9\")) {                    Plotly.newPlot(                        \"ea235245-9d5e-474b-9e4d-591f69c124e9\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"at=%{x}\\u003cbr\\u003eNumber of Reviews=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"xaxis\":\"x\",\"y\":[15,14,32,28,31,14,3],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"at\"},\"tickangle\":-45},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Number of Reviews\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Reviews for Week 2024-11-05 to 2024-11-11\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('ea235245-9d5e-474b-9e4d-591f69c124e9');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "daily_counts = df1.resample('D').size()"
      ],
      "metadata": {
        "id": "fIWh6JD1iVga"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fig = go.Figure()\n",
        "fig.add_trace(go.Bar(x=daily_counts.index, y=daily_counts.values,\n",
        "                     marker_color='skyblue'))\n",
        "fig.update_layout(title='Number of Reviews Day-wise',\n",
        "                  xaxis_title='Date',\n",
        "                  yaxis_title='Number of Reviews',\n",
        "                  xaxis_tickangle=-45)\n",
        "fig.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "3FpJA7Ynieo1",
        "outputId": "a79b5f98-0f54-4cb4-aaea-0848b3e4f95d"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"1bb7d113-0360-4142-be17-b7a29c342f9f\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"1bb7d113-0360-4142-be17-b7a29c342f9f\")) {                    Plotly.newPlot(                        \"1bb7d113-0360-4142-be17-b7a29c342f9f\",                        [{\"marker\":{\"color\":\"skyblue\"},\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"y\":[9,16,17,25,27,24,16,15,21,26,22,20,18,22,26,20,16,12,26,14,32,28,31,14,3],\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"title\":{\"text\":\"Date\"},\"tickangle\":-45},\"title\":{\"text\":\"Number of Reviews Day-wise\"},\"yaxis\":{\"title\":{\"text\":\"Number of Reviews\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('1bb7d113-0360-4142-be17-b7a29c342f9f');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = go.Figure()\n",
        "for source_name, source_data in df1.groupby('score'):\n",
        "    fig.add_trace(go.Scatter(x=source_data.resample('D').size().index, y=source_data.resample('D').size().values,\n",
        "                            mode='lines', name=source_name))\n",
        "fig.update_layout(title='Number of Reviews Day-wise',\n",
        "                  xaxis_title='Date',\n",
        "                  yaxis_title='Number of Reviews',\n",
        "                  xaxis_tickangle=-45)\n",
        "fig.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "q65z-B3eig8i",
        "outputId": "d3e8fcc2-b842-4f5a-9184-1ed094aa4154"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"35a061da-c14b-4fea-8bfb-aca1adc156d9\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"35a061da-c14b-4fea-8bfb-aca1adc156d9\")) {                    Plotly.newPlot(                        \"35a061da-c14b-4fea-8bfb-aca1adc156d9\",                        [{\"mode\":\"lines\",\"name\":\"1\",\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"y\":[3,6,11,11,10,5,7,5,3,13,9,8,3,6,7,5,6,4,10,5,15,7,6,5,1],\"type\":\"scatter\"},{\"mode\":\"lines\",\"name\":\"2\",\"x\":[\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\"],\"y\":[3,1,2,1,2,0,2,1,2,4,0,3,0,1,2,4,1,4,0,2,0,0,3],\"type\":\"scatter\"},{\"mode\":\"lines\",\"name\":\"3\",\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\"],\"y\":[1,0,2,1,3,0,0,1,1,1,1,0,1,1,1,1,2,2,3,0,1,3,4,1],\"type\":\"scatter\"},{\"mode\":\"lines\",\"name\":\"4\",\"x\":[\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"y\":[1,0,2,0,3,2,0,1,0,0,2,1,3,0,0,0,1,1,0,1,1,3,0,1],\"type\":\"scatter\"},{\"mode\":\"lines\",\"name\":\"5\",\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"y\":[5,6,3,9,13,14,7,7,15,10,8,10,10,12,17,12,4,4,8,9,13,17,18,5,1],\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"title\":{\"text\":\"Date\"},\"tickangle\":-45},\"title\":{\"text\":\"Number of Reviews Day-wise\"},\"yaxis\":{\"title\":{\"text\":\"Number of Reviews\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('35a061da-c14b-4fea-8bfb-aca1adc156d9');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = go.Figure()\n",
        "for rating_val, rating_data in df1.groupby('score'):\n",
        "    fig.add_trace(go.Scatter(x=rating_data.resample('D').size().index, y=rating_data.resample('D').size().values,\n",
        "                             mode='lines+markers', name=f'Rating {rating_val}'))\n",
        "fig.update_layout(title='Number of Reviews Day-wise by Rating',\n",
        "                  xaxis_title='Date',\n",
        "                  yaxis_title='Number of Reviews',\n",
        "                  xaxis_tickangle=-45)\n",
        "fig.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "beoS8EYskN02",
        "outputId": "8f7f9a0d-62a3-4a26-ee74-60a3e872c733"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"1bccb370-7ebe-4062-bcb9-6ca54fbf96f5\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"1bccb370-7ebe-4062-bcb9-6ca54fbf96f5\")) {                    Plotly.newPlot(                        \"1bccb370-7ebe-4062-bcb9-6ca54fbf96f5\",                        [{\"mode\":\"lines+markers\",\"name\":\"Rating 1\",\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"y\":[3,6,11,11,10,5,7,5,3,13,9,8,3,6,7,5,6,4,10,5,15,7,6,5,1],\"type\":\"scatter\"},{\"mode\":\"lines+markers\",\"name\":\"Rating 2\",\"x\":[\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\"],\"y\":[3,1,2,1,2,0,2,1,2,4,0,3,0,1,2,4,1,4,0,2,0,0,3],\"type\":\"scatter\"},{\"mode\":\"lines+markers\",\"name\":\"Rating 3\",\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\"],\"y\":[1,0,2,1,3,0,0,1,1,1,1,0,1,1,1,1,2,2,3,0,1,3,4,1],\"type\":\"scatter\"},{\"mode\":\"lines+markers\",\"name\":\"Rating 4\",\"x\":[\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"y\":[1,0,2,0,3,2,0,1,0,0,2,1,3,0,0,0,1,1,0,1,1,3,0,1],\"type\":\"scatter\"},{\"mode\":\"lines+markers\",\"name\":\"Rating 5\",\"x\":[\"2024-10-18T00:00:00\",\"2024-10-19T00:00:00\",\"2024-10-20T00:00:00\",\"2024-10-21T00:00:00\",\"2024-10-22T00:00:00\",\"2024-10-23T00:00:00\",\"2024-10-24T00:00:00\",\"2024-10-25T00:00:00\",\"2024-10-26T00:00:00\",\"2024-10-27T00:00:00\",\"2024-10-28T00:00:00\",\"2024-10-29T00:00:00\",\"2024-10-30T00:00:00\",\"2024-10-31T00:00:00\",\"2024-11-01T00:00:00\",\"2024-11-02T00:00:00\",\"2024-11-03T00:00:00\",\"2024-11-04T00:00:00\",\"2024-11-05T00:00:00\",\"2024-11-06T00:00:00\",\"2024-11-07T00:00:00\",\"2024-11-08T00:00:00\",\"2024-11-09T00:00:00\",\"2024-11-10T00:00:00\",\"2024-11-11T00:00:00\"],\"y\":[5,6,3,9,13,14,7,7,15,10,8,10,10,12,17,12,4,4,8,9,13,17,18,5,1],\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"title\":{\"text\":\"Date\"},\"tickangle\":-45},\"title\":{\"text\":\"Number of Reviews Day-wise by Rating\"},\"yaxis\":{\"title\":{\"text\":\"Number of Reviews\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('1bccb370-7ebe-4062-bcb9-6ca54fbf96f5');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['score']=df['score'].map({1:-1,2:-1,3:0,4:1,5:1})"
      ],
      "metadata": {
        "id": "b1o8giD8kchr"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "d992SY5Ukh11",
        "outputId": "eb2bd1de-278a-4540-9b3c-6c4dbfa70339"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                 reviewId        userName  \\\n",
              "0    869e82b7-735e-4615-8518-8afb85b59c18            Tina   \n",
              "1    c9145045-c36b-4ce3-93fd-0fe7feba4e12           Katie   \n",
              "2    089ee544-512e-403d-a363-cd978ba5bc95   Julie Cassady   \n",
              "3    6e111a29-3429-43f2-85f9-099873b4b2b3     Emily Regan   \n",
              "4    be858b2d-fd95-4fe5-9537-a6abfd839fd0         Terry K   \n",
              "..                                    ...             ...   \n",
              "495  015c06c5-e208-4dd0-9c66-245f36f5aa48  Keithen Booher   \n",
              "496  be8a0554-a37d-46d5-8504-24a15d879233        wolf07ga   \n",
              "497  7958eca8-72c9-48ef-9b6c-d7226447f88a  Nick Guzman G.   \n",
              "498  10a2b3b3-a420-4ba0-a748-0660e3ed677d    Vampiric Fae   \n",
              "499  47112154-0f61-4a79-bfa6-97667cd6993e             Bob   \n",
              "\n",
              "                                               content  score  thumbsUpCount  \\\n",
              "0    Love this site. I would rate it 5 stars as I h...      1              0   \n",
              "1    Fees are insane, I had 20 on my account went t...     -1              1   \n",
              "2    order was received as expected in a timely man...      1              0   \n",
              "3    GREAT APP!! I love to explore all of the diffe...      1              0   \n",
              "4                                      Excellent buyer      1              0   \n",
              "..                                                 ...    ...            ...   \n",
              "495                                 great shopping app      1              0   \n",
              "496  Fantastic place to shop that gives competition...      1              0   \n",
              "497  They used to be Good Now they charge you a ser...     -1              0   \n",
              "498  PLEASE GET RID OF THE GENERAL MESSAGING FEATUR...      0              3   \n",
              "499  I will not be using this app or platform again...     -1             18   \n",
              "\n",
              "    reviewCreatedVersion                  at  \n",
              "0                 8.16.0 2024-11-11 03:05:25  \n",
              "1                 8.24.1 2024-11-11 02:14:55  \n",
              "2                 8.24.1 2024-11-11 00:11:16  \n",
              "3                 8.24.1 2024-11-10 19:13:50  \n",
              "4                 8.24.1 2024-11-10 19:04:03  \n",
              "..                   ...                 ...  \n",
              "495               8.23.0 2024-10-18 19:28:20  \n",
              "496               8.23.0 2024-10-18 17:45:12  \n",
              "497               8.23.0 2024-10-18 16:37:01  \n",
              "498               8.22.0 2024-10-18 14:54:04  \n",
              "499               8.22.0 2024-10-18 14:12:20  \n",
              "\n",
              "[500 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-891fb954-1656-4d4f-9092-e61447791ad3\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>reviewId</th>\n",
              "      <th>userName</th>\n",
              "      <th>content</th>\n",
              "      <th>score</th>\n",
              "      <th>thumbsUpCount</th>\n",
              "      <th>reviewCreatedVersion</th>\n",
              "      <th>at</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>869e82b7-735e-4615-8518-8afb85b59c18</td>\n",
              "      <td>Tina</td>\n",
              "      <td>Love this site. I would rate it 5 stars as I h...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>8.16.0</td>\n",
              "      <td>2024-11-11 03:05:25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>c9145045-c36b-4ce3-93fd-0fe7feba4e12</td>\n",
              "      <td>Katie</td>\n",
              "      <td>Fees are insane, I had 20 on my account went t...</td>\n",
              "      <td>-1</td>\n",
              "      <td>1</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-11 02:14:55</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>089ee544-512e-403d-a363-cd978ba5bc95</td>\n",
              "      <td>Julie Cassady</td>\n",
              "      <td>order was received as expected in a timely man...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-11 00:11:16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>6e111a29-3429-43f2-85f9-099873b4b2b3</td>\n",
              "      <td>Emily Regan</td>\n",
              "      <td>GREAT APP!! I love to explore all of the diffe...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-10 19:13:50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>be858b2d-fd95-4fe5-9537-a6abfd839fd0</td>\n",
              "      <td>Terry K</td>\n",
              "      <td>Excellent buyer</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>8.24.1</td>\n",
              "      <td>2024-11-10 19:04:03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>015c06c5-e208-4dd0-9c66-245f36f5aa48</td>\n",
              "      <td>Keithen Booher</td>\n",
              "      <td>great shopping app</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>8.23.0</td>\n",
              "      <td>2024-10-18 19:28:20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>be8a0554-a37d-46d5-8504-24a15d879233</td>\n",
              "      <td>wolf07ga</td>\n",
              "      <td>Fantastic place to shop that gives competition...</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>8.23.0</td>\n",
              "      <td>2024-10-18 17:45:12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>7958eca8-72c9-48ef-9b6c-d7226447f88a</td>\n",
              "      <td>Nick Guzman G.</td>\n",
              "      <td>They used to be Good Now they charge you a ser...</td>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>8.23.0</td>\n",
              "      <td>2024-10-18 16:37:01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>10a2b3b3-a420-4ba0-a748-0660e3ed677d</td>\n",
              "      <td>Vampiric Fae</td>\n",
              "      <td>PLEASE GET RID OF THE GENERAL MESSAGING FEATUR...</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>8.22.0</td>\n",
              "      <td>2024-10-18 14:54:04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>47112154-0f61-4a79-bfa6-97667cd6993e</td>\n",
              "      <td>Bob</td>\n",
              "      <td>I will not be using this app or platform again...</td>\n",
              "      <td>-1</td>\n",
              "      <td>18</td>\n",
              "      <td>8.22.0</td>\n",
              "      <td>2024-10-18 14:12:20</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 7 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-891fb954-1656-4d4f-9092-e61447791ad3')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-891fb954-1656-4d4f-9092-e61447791ad3 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-891fb954-1656-4d4f-9092-e61447791ad3');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-ace516af-3487-417b-aa2f-653876f8ee78\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-ace516af-3487-417b-aa2f-653876f8ee78')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-ace516af-3487-417b-aa2f-653876f8ee78 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_9e6b3aeb-145a-48a0-a88e-468d1e48dc16\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_9e6b3aeb-145a-48a0-a88e-468d1e48dc16 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 500,\n  \"fields\": [\n    {\n      \"column\": \"reviewId\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 500,\n        \"samples\": [\n          \"e06329ef-9253-4acf-a6c6-664bdc9f5f88\",\n          \"f4a3b38d-5fd9-488e-b4af-6a9eb733c68e\",\n          \"950512a2-ecdb-4204-816b-97587ecce198\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"userName\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 499,\n        \"samples\": [\n          \"Maryam Abubakar\",\n          \"Lynzi Edwards\",\n          \"Eric Thompson\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"content\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 491,\n        \"samples\": [\n          \"due to fees charged by Mercari, one can now expect go pay 1/3 to 1/2 more than the asking price.\",\n          \"Ever since Mercari started charging the buyer for all fees, my sales have gone down tremendously. They also allow buyers to get away with things without properly investigating and do not give the seller the benefit of the doubt. I am so disappointed in the current platform.\",\n          \"I'm very happy to be a part of Mecari . Great communication.. No complaints.\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"score\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": -1,\n        \"max\": 1,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          -1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"thumbsUpCount\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 16,\n        \"min\": 0,\n        \"max\": 265,\n        \"num_unique_values\": 23,\n        \"samples\": [\n          265,\n          29,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"reviewCreatedVersion\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 22,\n        \"samples\": [\n          \"8.16.0\",\n          \"7.82.0\",\n          \"8.9.0\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"at\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"2024-10-18 14:12:20\",\n        \"max\": \"2024-11-11 03:05:25\",\n        \"num_unique_values\": 500,\n        \"samples\": [\n          \"2024-10-25 08:10:20\",\n          \"2024-11-08 01:44:37\",\n          \"2024-10-24 14:38:46\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_new = df[['content', 'score']]"
      ],
      "metadata": {
        "id": "J1sIjI-gk0Oi"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new['score'].unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wG9t73Vpk6xD",
        "outputId": "ee9958d1-a786-4a7d-bb92-05d420c22006"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 1, -1,  0])"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig = go.Figure(data=[go.Bar(x=df_new['score'].value_counts().index, y=df_new['score'].value_counts())])\n",
        "fig.update_layout(title='Rating',xaxis_title=\"Rating\",yaxis_title=\"Count\")\n",
        "fig.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "NG3F9hsbk_Os",
        "outputId": "76994839-41c4-405e-ce23-c29a095940c1"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"d549a38c-0074-40f5-9afe-6fe423ef421f\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"d549a38c-0074-40f5-9afe-6fe423ef421f\")) {                    Plotly.newPlot(                        \"d549a38c-0074-40f5-9afe-6fe423ef421f\",                        [{\"x\":[1,-1,0],\"y\":[260,209,31],\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"title\":{\"text\":\"Rating\"},\"xaxis\":{\"title\":{\"text\":\"Rating\"}},\"yaxis\":{\"title\":{\"text\":\"Count\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('d549a38c-0074-40f5-9afe-6fe423ef421f');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "counts = df_new['score'].value_counts()\n",
        "fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts)])\n",
        "fig.update_layout(title='Rating')\n",
        "fig.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "WDPYY0eklDp9",
        "outputId": "bb8b47f4-f315-4a8f-b1e1-1b52831c121d"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"d591ebd0-39aa-4a0d-b417-64e9846360b7\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"d591ebd0-39aa-4a0d-b417-64e9846360b7\")) {                    Plotly.newPlot(                        \"d591ebd0-39aa-4a0d-b417-64e9846360b7\",                        [{\"labels\":[1,-1,0],\"values\":[260,209,31],\"type\":\"pie\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"title\":{\"text\":\"Rating\"}},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('d591ebd0-39aa-4a0d-b417-64e9846360b7');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#NLP"
      ],
      "metadata": {
        "id": "coBg5EP_lMte"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def clean_text(text):\n",
        "  text = text.lower()\n",
        "  return text.strip()"
      ],
      "metadata": {
        "id": "NAgfSmCklMNF"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x: clean_text(x))"
      ],
      "metadata": {
        "id": "vj5ASEHSlWis"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "4UrLKznQleba",
        "outputId": "d092a911-e6d7-4ae5-fc30-5bc31fe70f67"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      love this site. i would rate it 5 stars as i h...\n",
              "1      fees are insane, i had 20 on my account went t...\n",
              "2      order was received as expected in a timely man...\n",
              "3      great app!! i love to explore all of the diffe...\n",
              "4                                        excellent buyer\n",
              "                             ...                        \n",
              "495                                   great shopping app\n",
              "496    fantastic place to shop that gives competition...\n",
              "497    they used to be good now they charge you a ser...\n",
              "498    please get rid of the general messaging featur...\n",
              "499    i will not be using this app or platform again...\n",
              "Name: content, Length: 500, dtype: object"
            ],
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
              "      <th>content</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>love this site. i would rate it 5 stars as i h...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>fees are insane, i had 20 on my account went t...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>order was received as expected in a timely man...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>great app!! i love to explore all of the diffe...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>excellent buyer</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>great shopping app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>fantastic place to shop that gives competition...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>they used to be good now they charge you a ser...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>please get rid of the general messaging featur...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>i will not be using this app or platform again...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 1 columns</p>\n",
              "</div><br><label><b>dtype:</b> object</label>"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import string\n",
        "string.punctuation"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "mnlK5atClhq4",
        "outputId": "d650f96d-094b-4cb6-c880-e8dd8ddb270b"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'!\"#$%&\\'()*+,-./:;<=>?@[\\\\]^_`{|}~'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_punctuation(text):\n",
        "    punctuationfree=\"\".join([i for i in text if i not in string.punctuation])\n",
        "    return punctuationfree"
      ],
      "metadata": {
        "id": "toD3MObullkf"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x:remove_punctuation(x))"
      ],
      "metadata": {
        "id": "45vCEk0dlpRp"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x: x.lower())"
      ],
      "metadata": {
        "id": "Pat1cMJiluSE"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import re"
      ],
      "metadata": {
        "id": "SaDMORE6lyxe"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def tokenization(text):\n",
        "    tokens = re.split(' ',text)\n",
        "    return tokens"
      ],
      "metadata": {
        "id": "Y5puuEBHl06l"
      },
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x: tokenization(x))"
      ],
      "metadata": {
        "id": "lptCh6QAl3Ms"
      },
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "GCiS4KQyl9Tz",
        "outputId": "df57cfe8-6720-436d-e6aa-a076c9bbc589"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      [love, this, site, i, would, rate, it, 5, star...\n",
              "1      [fees, are, insane, i, had, 20, on, my, accoun...\n",
              "2      [order, was, received, as, expected, in, a, ti...\n",
              "3      [great, app, i, love, to, explore, all, of, th...\n",
              "4                                     [excellent, buyer]\n",
              "                             ...                        \n",
              "495                               [great, shopping, app]\n",
              "496    [fantastic, place, to, shop, that, gives, comp...\n",
              "497    [they, used, to, be, good, now, they, charge, ...\n",
              "498    [please, get, rid, of, the, general, messaging...\n",
              "499    [i, will, not, be, using, this, app, or, platf...\n",
              "Name: content, Length: 500, dtype: object"
            ],
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
              "      <th>content</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>[love, this, site, i, would, rate, it, 5, star...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>[fees, are, insane, i, had, 20, on, my, accoun...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>[order, was, received, as, expected, in, a, ti...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>[great, app, i, love, to, explore, all, of, th...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>[excellent, buyer]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>[great, shopping, app]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>[fantastic, place, to, shop, that, gives, comp...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>[they, used, to, be, good, now, they, charge, ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>[please, get, rid, of, the, general, messaging...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>[i, will, not, be, using, this, app, or, platf...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 1 columns</p>\n",
              "</div><br><label><b>dtype:</b> object</label>"
            ]
          },
          "metadata": {},
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk\n",
        "nltk.download('stopwords')\n",
        "stopwords = nltk.corpus.stopwords.words('english')\n",
        "stopwords[0:10]\n",
        "['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', \"you're\"]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "27KBiCHtmBH7",
        "outputId": "48b7e032-fe2b-4aee-de78-b50ff6f59374"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/stopwords.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', \"you're\"]"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_stopwords(text):\n",
        "    output= \" \".join(i for i in text if i not in stopwords)\n",
        "    return output"
      ],
      "metadata": {
        "id": "0ttXEhUdmErT"
      },
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x:remove_stopwords(x))"
      ],
      "metadata": {
        "id": "Q_0L8LOzmHPf"
      },
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "YvGBwONnmMZf",
        "outputId": "e85a5ba1-9c99-44f1-b2a5-51da09972040"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      love site would rate 5 stars bought many items...\n",
              "1      fees insane 20 account went buy item 68 dollar...\n",
              "2                  order received expected timely manner\n",
              "3      great app love explore different items sale bo...\n",
              "4                                        excellent buyer\n",
              "                             ...                        \n",
              "495                                   great shopping app\n",
              "496    fantastic place shop gives competition online ...\n",
              "497    used good charge service fee processing paymen...\n",
              "498    please get rid general messaging feature news ...\n",
              "499    using app platform problems accepting payment ...\n",
              "Name: content, Length: 500, dtype: object"
            ],
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
              "      <th>content</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>love site would rate 5 stars bought many items...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>fees insane 20 account went buy item 68 dollar...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>order received expected timely manner</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>great app love explore different items sale bo...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>excellent buyer</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>great shopping app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>fantastic place shop gives competition online ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>used good charge service fee processing paymen...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>please get rid general messaging feature news ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>using app platform problems accepting payment ...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 1 columns</p>\n",
              "</div><br><label><b>dtype:</b> object</label>"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def clean_text(text):\n",
        "    text = re.sub('\\[.*\\]','', text).strip()\n",
        "    text = re.sub('\\S*\\d\\S*\\s*','', text).strip()\n",
        "    return text.strip()"
      ],
      "metadata": {
        "id": "vpCtmHfMmPwc"
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x: clean_text(x))"
      ],
      "metadata": {
        "id": "967DpFCGmSkm"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "YweWN3xLmY9z",
        "outputId": "2f9de232-b322-4dbf-b3d3-0671631e9e36"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      love site would rate stars bought many items e...\n",
              "1      fees insane account went buy item dollars tota...\n",
              "2                  order received expected timely manner\n",
              "3      great app love explore different items sale bo...\n",
              "4                                        excellent buyer\n",
              "                             ...                        \n",
              "495                                   great shopping app\n",
              "496    fantastic place shop gives competition online ...\n",
              "497    used good charge service fee processing paymen...\n",
              "498    please get rid general messaging feature news ...\n",
              "499    using app platform problems accepting payment ...\n",
              "Name: content, Length: 500, dtype: object"
            ],
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
              "      <th>content</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>love site would rate stars bought many items e...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>fees insane account went buy item dollars tota...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>order received expected timely manner</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>great app love explore different items sale bo...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>excellent buyer</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>great shopping app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>fantastic place shop gives competition online ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>used good charge service fee processing paymen...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>please get rid general messaging feature news ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>using app platform problems accepting payment ...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 1 columns</p>\n",
              "</div><br><label><b>dtype:</b> object</label>"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import spacy\n",
        "nlp = spacy.load('en_core_web_sm')"
      ],
      "metadata": {
        "id": "eY0jwyVBmbZ9"
      },
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "stopwords = nlp.Defaults.stop_words\n",
        "def lemmatizer(text):\n",
        "    doc = nlp(text)\n",
        "    sent = [token.lemma_ for token in doc if not token.text in set(stopwords)]\n",
        "    return ' '.join(sent)\n",
        "  #stemmimg will give root word but not necesserily meaningful\n",
        "  #but lemmetization will give root word which is meaningful"
      ],
      "metadata": {
        "id": "9rnIXkgOmehB"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content =  df_new.content.apply(lambda x: lemmatizer(x))"
      ],
      "metadata": {
        "id": "hZDlJ8IdmoP7"
      },
      "execution_count": 48,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "5ohup9iemrsZ",
        "outputId": "6277b951-b147-4a70-bf51-752d28a2437a"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      love site rate star buy item additional fee ad...\n",
              "1      fee insane account go buy item dollar total do...\n",
              "2                     order receive expect timely manner\n",
              "3      great app love explore different item sale buy...\n",
              "4                                        excellent buyer\n",
              "                             ...                        \n",
              "495                                   great shopping app\n",
              "496    fantastic place shop give competition online s...\n",
              "497       good charge service fee processing payment fee\n",
              "498    rid general message feature news seller especi...\n",
              "499    app platform problem accept payment paypal com...\n",
              "Name: content, Length: 500, dtype: object"
            ],
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
              "      <th>content</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>love site rate star buy item additional fee ad...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>fee insane account go buy item dollar total do...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>order receive expect timely manner</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>great app love explore different item sale buy...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>excellent buyer</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>great shopping app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>fantastic place shop give competition online s...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>good charge service fee processing payment fee</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>rid general message feature news seller especi...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>app platform problem accept payment paypal com...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 1 columns</p>\n",
              "</div><br><label><b>dtype:</b> object</label>"
            ]
          },
          "metadata": {},
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_urls(vTEXT):\n",
        "    vTEXT = re.sub(r'(https|http)?:\\/\\/(\\w|\\.|\\/|\\?|\\=|\\&|\\%)*\\b', '', vTEXT, flags=re.MULTILINE)\n",
        "    return(vTEXT)"
      ],
      "metadata": {
        "id": "nux4CfHRmwJ0"
      },
      "execution_count": 50,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x: remove_urls(x))"
      ],
      "metadata": {
        "id": "WOPPYDGzmynF"
      },
      "execution_count": 51,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_digits(text):\n",
        "    clean_text = re.sub(r\"\\b[0-9]+\\b\\s*\", \"\", text)\n",
        "    return(text)"
      ],
      "metadata": {
        "id": "4ogPiRa_m5op"
      },
      "execution_count": 52,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content = df_new.content.apply(lambda x: remove_digits(x))"
      ],
      "metadata": {
        "id": "R9tnTCaZm9K2"
      },
      "execution_count": 53,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_digits1(sample_text):\n",
        "    clean_text = \" \".join([w for w in sample_text.split() if not w.isdigit()])\n",
        "    return(clean_text)"
      ],
      "metadata": {
        "id": "UTRMNeponEbG"
      },
      "execution_count": 54,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new.content= df_new.content.apply(lambda x: remove_digits1(x))"
      ],
      "metadata": {
        "id": "H_sBXGipnFa0"
      },
      "execution_count": 55,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_emojis(data):\n",
        "    emoji_pattern = re.compile(\"[\"\n",
        "                               u\"\\U0001F600-\\U0001F64F\"\n",
        "                               u\"\\U0001F300-\\U0001F5FF\"\n",
        "                               u\"\\U0001F680-\\U0001F6FF\"\n",
        "                               u\"\\U0001F1E0-\\U0001F1FF\"\n",
        "                               \"]+\", flags=re.UNICODE)\n",
        "    return re.sub(emoji_pattern, '', data)"
      ],
      "metadata": {
        "id": "MtvDYF3RnP78"
      },
      "execution_count": 56,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_new"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "B3GkxR-TnSE4",
        "outputId": "cba8844b-37e1-4dcf-dace-e43cca8bbed8"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                               content  score\n",
              "0    love site rate star buy item additional fee ad...      1\n",
              "1    fee insane account go buy item dollar total do...     -1\n",
              "2                   order receive expect timely manner      1\n",
              "3    great app love explore different item sale buy...      1\n",
              "4                                      excellent buyer      1\n",
              "..                                                 ...    ...\n",
              "495                                 great shopping app      1\n",
              "496  fantastic place shop give competition online s...      1\n",
              "497     good charge service fee processing payment fee     -1\n",
              "498  rid general message feature news seller especi...      0\n",
              "499  app platform problem accept payment paypal com...     -1\n",
              "\n",
              "[500 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-595f1baf-4500-4baa-9d3b-55c8db5d04ab\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>content</th>\n",
              "      <th>score</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>love site rate star buy item additional fee ad...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>fee insane account go buy item dollar total do...</td>\n",
              "      <td>-1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>order receive expect timely manner</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>great app love explore different item sale buy...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>excellent buyer</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>great shopping app</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>fantastic place shop give competition online s...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>good charge service fee processing payment fee</td>\n",
              "      <td>-1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>rid general message feature news seller especi...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>app platform problem accept payment paypal com...</td>\n",
              "      <td>-1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 2 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-595f1baf-4500-4baa-9d3b-55c8db5d04ab')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-595f1baf-4500-4baa-9d3b-55c8db5d04ab button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-595f1baf-4500-4baa-9d3b-55c8db5d04ab');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-7476f580-8b2b-4875-928d-e8ce2e556797\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-7476f580-8b2b-4875-928d-e8ce2e556797')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-7476f580-8b2b-4875-928d-e8ce2e556797 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_a8640259-4c1d-4d30-ae8c-cdd0434932ff\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df_new')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_a8640259-4c1d-4d30-ae8c-cdd0434932ff button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df_new');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df_new",
              "summary": "{\n  \"name\": \"df_new\",\n  \"rows\": 500,\n  \"fields\": [\n    {\n      \"column\": \"content\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 471,\n        \"samples\": [\n          \"excellent place buy overseas item anime game etc\",\n          \"cool place buy sell enjoy app\",\n          \"better\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"score\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": -1,\n        \"max\": 1,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          -1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import wordcloud"
      ],
      "metadata": {
        "id": "wu1uz0-XnU2s"
      },
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from wordcloud import WordCloud\n",
        "data = df_new.content\n",
        "plt.figure(figsize = (20,20))\n",
        "wc = WordCloud(max_words = 1000 , width = 1600 , height = 800,\n",
        "               collocations=False).generate(\" \".join(data))\n",
        "plt.imshow(wc)\n",
        "plt.axis('off')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 768
        },
        "id": "gWLeh3m6nW5I",
        "outputId": "c28603d8-e5a9-475c-ede8-06af9665cafd"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 2000x2000 with 1 Axes>"
            ],
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from wordcloud import WordCloud\n",
        "data = df_new[df_new['score'] == 1]['content']\n",
        "plt.figure(figsize = (20,20))\n",
        "wc = WordCloud(max_words = 1000 , width = 1600 , height = 800,\n",
        "               collocations=False).generate(\" \".join(data))\n",
        "plt.imshow(wc)\n",
        "plt.axis('off')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 768
        },
        "id": "7WRRQj9OnhXk",
        "outputId": "2a8955e6-75a1-4d27-eebf-c4d94a7a0507"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 2000x2000 with 1 Axes>"
            ],
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_extraction.text import TfidfVectorizer"
      ],
      "metadata": {
        "id": "xBj_DOSxnvSr"
      },
      "execution_count": 61,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tf1=TfidfVectorizer()\n",
        "data_vec=tf1.fit_transform(df_new['content'])"
      ],
      "metadata": {
        "id": "pG96PWRCn3x4"
      },
      "execution_count": 62,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data_vec"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FzHneNPSn525",
        "outputId": "236b0bae-32f6-40a4-ae7e-534adde378e3"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<500x1449 sparse matrix of type '<class 'numpy.float64'>'\n",
              "\twith 5757 stored elements in Compressed Sparse Row format>"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle"
      ],
      "metadata": {
        "id": "FurzQtEvn7qr"
      },
      "execution_count": 64,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open ('tfidf_vectorizer.pkl','wb') as model_file:\n",
        "    pickle.dump(tf1, model_file)   #in a dump file the contents can not be understood, serilisation deserialisation of the dtata"
      ],
      "metadata": {
        "id": "Cf55U4xAn_UO"
      },
      "execution_count": 65,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y=df_new['score'].values"
      ],
      "metadata": {
        "id": "meRmiUdkoDgD"
      },
      "execution_count": 66,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.svm import SVC\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.ensemble import AdaBoostClassifier\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "GO69Pr_ioFVn"
      },
      "execution_count": 67,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train,X_test,y_train,y_test=train_test_split(data_vec,y,test_size=0.2,stratify = y, random_state=42)"
      ],
      "metadata": {
        "id": "ay-z80y6oJ70"
      },
      "execution_count": 68,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from imblearn.over_sampling import SMOTE"
      ],
      "metadata": {
        "id": "0URLv_yJoL5z"
      },
      "execution_count": 69,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "smote = SMOTE(random_state=42)\n",
        "X_balanced, y_balanced = smote.fit_resample(X_train, y_train)\n",
        "#if two classes data are not in equal proportions or quantities then we use smote to balance thheir number of imgs/workds"
      ],
      "metadata": {
        "id": "C1EbD_C4oVdb"
      },
      "execution_count": 70,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report"
      ],
      "metadata": {
        "id": "_8hVo41loWqg"
      },
      "execution_count": 71,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sv = SVC()\n",
        "dt = DecisionTreeClassifier()\n",
        "rf = RandomForestClassifier()\n",
        "ad = AdaBoostClassifier()\n",
        "\n",
        "models = [sv, dt, rf, ad]\n",
        "\n",
        "accuracies = []\n",
        "\n",
        "for model in models:\n",
        "    print('Results for the model:', model.__class__.__name__)\n",
        "    model.fit(X_balanced, y_balanced)\n",
        "    y_pred = model.predict(X_test)\n",
        "\n",
        "    accuracy = accuracy_score(y_test, y_pred)\n",
        "    print('Accuracy:', accuracy)\n",
        "\n",
        "    cm = confusion_matrix(y_test, y_pred)\n",
        "    print('Confusion Matrix:\\n', cm)\n",
        "\n",
        "    report = classification_report(y_test, y_pred)\n",
        "    print('Classification Report:\\n', report)\n",
        "\n",
        "    print('\\n')\n",
        "\n",
        "    accuracies.append(accuracy)\n",
        "\n",
        "print('List of Accuracies:', accuracies)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NeCXqDbaoY7k",
        "outputId": "ea6057fb-f224-4d24-e448-fe4e90bed7b6"
      },
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Results for the model: SVC\n",
            "Accuracy: 0.86\n",
            "Confusion Matrix:\n",
            " [[36  0  6]\n",
            " [ 3  0  3]\n",
            " [ 2  0 50]]\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "          -1       0.88      0.86      0.87        42\n",
            "           0       0.00      0.00      0.00         6\n",
            "           1       0.85      0.96      0.90        52\n",
            "\n",
            "    accuracy                           0.86       100\n",
            "   macro avg       0.58      0.61      0.59       100\n",
            "weighted avg       0.81      0.86      0.83       100\n",
            "\n",
            "\n",
            "\n",
            "Results for the model: DecisionTreeClassifier\n",
            "Accuracy: 0.78\n",
            "Confusion Matrix:\n",
            " [[30  4  8]\n",
            " [ 1  2  3]\n",
            " [ 5  1 46]]\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "          -1       0.83      0.71      0.77        42\n",
            "           0       0.29      0.33      0.31         6\n",
            "           1       0.81      0.88      0.84        52\n",
            "\n",
            "    accuracy                           0.78       100\n",
            "   macro avg       0.64      0.64      0.64       100\n",
            "weighted avg       0.79      0.78      0.78       100\n",
            "\n",
            "\n",
            "\n",
            "Results for the model: RandomForestClassifier\n",
            "Accuracy: 0.83\n",
            "Confusion Matrix:\n",
            " [[33  0  9]\n",
            " [ 2  0  4]\n",
            " [ 2  0 50]]\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "          -1       0.89      0.79      0.84        42\n",
            "           0       0.00      0.00      0.00         6\n",
            "           1       0.79      0.96      0.87        52\n",
            "\n",
            "    accuracy                           0.83       100\n",
            "   macro avg       0.56      0.58      0.57       100\n",
            "weighted avg       0.79      0.83      0.80       100\n",
            "\n",
            "\n",
            "\n",
            "Results for the model: AdaBoostClassifier\n",
            "Accuracy: 0.73\n",
            "Confusion Matrix:\n",
            " [[28  2 12]\n",
            " [ 2  0  4]\n",
            " [ 7  0 45]]\n",
            "Classification Report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "          -1       0.76      0.67      0.71        42\n",
            "           0       0.00      0.00      0.00         6\n",
            "           1       0.74      0.87      0.80        52\n",
            "\n",
            "    accuracy                           0.73       100\n",
            "   macro avg       0.50      0.51      0.50       100\n",
            "weighted avg       0.70      0.73      0.71       100\n",
            "\n",
            "\n",
            "\n",
            "List of Accuracies: [0.86, 0.78, 0.83, 0.73]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle"
      ],
      "metadata": {
        "id": "MX_eZsBjozxt"
      },
      "execution_count": 73,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sv=SVC()\n",
        "model_sv =  sv.fit(X_balanced, y_balanced)\n",
        "model_filename = 'svm_model.pkl'\n",
        "with open(model_filename, 'wb') as model_file:\n",
        "    pickle.dump(model_sv,model_file)"
      ],
      "metadata": {
        "id": "YG1faFw3o2Ys"
      },
      "execution_count": 74,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_names = ['SVC', 'DecisionTree', 'RandomForest', 'AdaBoost']\n",
        "fig = go.Figure(data=go.Bar(x=model_names, y=accuracies))\n",
        "fig.update_layout(title='Model Accuracies',\n",
        "                  xaxis_title='Model',\n",
        "                  yaxis_title='Accuracy',\n",
        "                  yaxis_tickformat='.2%',\n",
        "                  yaxis_range=[0, 1],\n",
        "                  xaxis_tickangle=0)\n",
        "fig.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "e9F7Onmuo5Ab",
        "outputId": "a66c6483-fe46-4d29-e054-0629de7991f5"
      },
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.35.2.min.js\"></script>                <div id=\"515be86c-8c7c-4d9f-a7ea-827b667a60af\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"515be86c-8c7c-4d9f-a7ea-827b667a60af\")) {                    Plotly.newPlot(                        \"515be86c-8c7c-4d9f-a7ea-827b667a60af\",                        [{\"x\":[\"SVC\",\"DecisionTree\",\"RandomForest\",\"AdaBoost\"],\"y\":[0.86,0.78,0.83,0.73],\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"yaxis\":{\"title\":{\"text\":\"Accuracy\"},\"tickformat\":\".2%\",\"range\":[0,1]},\"xaxis\":{\"title\":{\"text\":\"Model\"},\"tickangle\":0},\"title\":{\"text\":\"Model Accuracies\"}},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('515be86c-8c7c-4d9f-a7ea-827b667a60af');\n",
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
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_filename = 'svm_model.pkl'\n",
        "with open(model_filename,'wb') as model_file:\n",
        "  pickle.dump(model_sv,model_file)"
      ],
      "metadata": {
        "id": "Y_K-qKxYo8Ru"
      },
      "execution_count": 76,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rwfX2s9zo-vR",
        "outputId": "3a59f3fc-41e7-46b0-a4a5-54f0ebf08861"
      },
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.40.1-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (10.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.4.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.1)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.40.1-py2.py3-none-any.whl (8.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.6/8.6 MB\u001b[0m \u001b[31m53.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m61.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m8.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.40.1 watchdog-6.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pickle\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "from PIL import Image\n",
        "import re\n",
        "import string\n",
        "import nltk\n",
        "import spacy\n",
        "import sklearn\n",
        "import joblib\n",
        "\n",
        "# Check the version of Streamlit\n",
        "print(f\"Streamlit version: {st.__version__}\")\n",
        "\n",
        "# Check the version of PIL (Pillow)\n",
        "pillow_version = Image.__version__\n",
        "print(f\"Pillow version: {pillow_version}\")\n",
        "\n",
        "# Check the version of re (regular expressions)\n",
        "print(f\"Python re (regular expressions) version: {re.__version__}\")\n",
        "\n",
        "# Check the version of NLTK (Natural Language Toolkit)\n",
        "nltk_version = nltk.__version__\n",
        "print(f\"NLTK version: {nltk_version}\")\n",
        "\n",
        "# Check the version of spaCy\n",
        "spacy_version = spacy.__version__\n",
        "print(f\"spaCy version: {spacy_version}\")\n",
        "\n",
        "# Check the version of scikit-learn\n",
        "sklearn_version = sklearn.__version__\n",
        "print(f\"scikit-learn version: {sklearn_version}\")\n",
        "\n",
        "# Check the version of joblib\n",
        "joblib_version = joblib.__version__\n",
        "print(f\"joblib version: {joblib_version}\")"
      ],
      "metadata": {
        "id": "9gqs3yh_pB-j",
        "outputId": "55576734-a48a-4509-adbe-2744cbff2995",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Streamlit version: 1.40.1\n",
            "Pillow version: 10.4.0\n",
            "Python re (regular expressions) version: 2.2.1\n",
            "NLTK version: 3.8.1\n",
            "spaCy version: 3.7.5\n",
            "scikit-learn version: 1.5.2\n",
            "joblib version: 1.4.2\n"
          ]
        }
      ]
    }
  ]
}