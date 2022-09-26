{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "McSxJAwcOdZ1"
      },
      "source": [
        "# Basic Python"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CU48hgo4Owz5"
      },
      "source": [
        "## 1. Split this string"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "s07c7JK7Oqt-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "28a48f50-88fd-4419-813e-817c5d2007ea"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hi', 'there', 'Sam!']\n"
          ]
        }
      ],
      "source": [
        "s = \"Hi there Sam!\"\n",
        "print(s.split())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GH1QBn8HP375"
      },
      "source": [
        "## 2. Use .format() to print the following string. \n",
        "\n",
        "### Output should be: The diameter of Earth is 12742 kilometers."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "_ZHoml3kPqic"
      },
      "outputs": [],
      "source": [
        "planet = \"Earth\"\n",
        "diameter = 12742"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "HyRyJv6CYPb4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "65985877-4570-4e5d-e266-c6784875f1cb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The diameter of Earth is 12742 kilometres.\n"
          ]
        }
      ],
      "source": [
        "txt=\"The diameter of {plt} is {dr} kilometres.\".format(plt=planet,dr=diameter)\n",
        "print(txt)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KE74ZEwkRExZ"
      },
      "source": [
        "## 3. In this nest dictionary grab the word \"hello\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "fcVwbCc1QrQI"
      },
      "outputs": [],
      "source": [
        "d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "MvbkMZpXYRaw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "35494bc2-d4e5-4ff6-bc45-c961e11c8dbe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello\n"
          ]
        }
      ],
      "source": [
        "print(d['k1'][3]['tricky'][3]['target'][3])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bw0vVp-9ddjv"
      },
      "source": [
        "# Numpy"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "LLiE_TYrhA1O"
      },
      "outputs": [],
      "source": [
        "import numpy as np"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wOg8hinbgx30"
      },
      "source": [
        "## 4.1 Create an array of 10 zeros? \n",
        "## 4.2 Create an array of 10 fives?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "NHrirmgCYXvU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b14d7b10-2e5a-4341-b28c-05c7c84c6066"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\n"
          ]
        }
      ],
      "source": [
        "array=np.zeros(10)\n",
        "print(array)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "e4005lsTYXxx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d248369d-eba6-4847-dd11-23c58fd591a5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]\n"
          ]
        }
      ],
      "source": [
        "array=np.ones(10)*5\n",
        "print(array)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gZHHDUBvrMX4"
      },
      "source": [
        "## 5. Create an array of all the even integers from 20 to 35"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "oAI2tbU2Yag-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3c11078a-0879-44f1-9bd4-6906d1c49376"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[20 22 24 26 28 30 32 34]\n"
          ]
        }
      ],
      "source": [
        "array=np.arange(20,35,2)\n",
        "print(array)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NaOM308NsRpZ"
      },
      "source": [
        "## 6. Create a 3x3 matrix with values ranging from 0 to 8"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jZVvHZ3Xe2r0",
        "outputId": "3c212bfa-dc7f-4b5c-c910-6d1e2aa9cce2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0 1 2]\n",
            " [3 4 5]\n",
            " [6 7 8]]\n"
          ]
        }
      ],
      "source": [
        "arr=np.arange(0,9).reshape(3,3)\n",
        "print(arr)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hQ0dnhAQuU_p"
      },
      "source": [
        "## 7. Concatinate a and b \n",
        "## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "rAPSw97aYfE0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6cb8b195-d246-45ce-ef02-8c0071779a69"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 2, 3, 4, 5, 6])"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ],
      "source": [
        "a=np.array([1,2,3])\n",
        "b=np.array([4,5,6])\n",
        "np.concatenate([a,b])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dlPEY9DRwZga"
      },
      "source": [
        "# Pandas"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ijoYW51zwr87"
      },
      "source": [
        "## 8. Create a dataframe with 3 rows and 2 columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "T5OxJRZ8uvR7"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "xNpI_XXoYhs0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a56b0fad-bade-477b-c6fa-ce3292979061"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     0    1\n",
            "0  NaN  NaN\n",
            "1  NaN  NaN\n",
            "2  NaN  NaN\n"
          ]
        }
      ],
      "source": [
        "data=pd.DataFrame(index=np.arange(3), columns=np.arange(2))\n",
        "print(data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UXSmdNclyJQD"
      },
      "source": [
        "## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "dgyC0JhVYl4F",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9e7b04dd-4cb8-4b1f-cfbf-371f1fca2902"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',\n",
            "               '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',\n",
            "               '2023-01-09', '2023-01-10',\n",
            "               ...\n",
            "               '2023-09-23', '2023-09-24', '2023-09-25', '2023-09-26',\n",
            "               '2023-09-27', '2023-09-28', '2023-09-29', '2023-09-30',\n",
            "               '2023-10-01', '2023-10-02'],\n",
            "              dtype='datetime64[ns]', length=275, freq='D')\n"
          ]
        }
      ],
      "source": [
        "data=pd.date_range(start=\"1/1/2023\",end=\"10/2/2023\")\n",
        "print(data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZizSetD-y5az"
      },
      "source": [
        "## 10. Create 2D list to DataFrame\n",
        "\n",
        "lists = [[1, 'aaa', 22],\n",
        "         [2, 'bbb', 25],\n",
        "         [3, 'ccc', 24]]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "id": "_XMC8aEt0llB"
      },
      "outputs": [],
      "source": [
        "lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "knH76sDKYsVX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7b25fedc-6103-43e2-8394-5e869556a585"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   s.no pattern  number\n",
            "0     1     aaa      22\n",
            "1     2     bbb      25\n",
            "2     3     ccc      24\n"
          ]
        }
      ],
      "source": [
        "data=pd.DataFrame(lists,columns=[\"s.no\",\"pattern\",\"number\"])\n",
        "print(data)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3.10.5 64-bit",
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
      "version": "3.10.5"
    },
    "vscode": {
      "interpreter": {
        "hash": "e33dda8a4d12c9c36a233218a905238da2bb40652a11ab3365bb0fe0ea2bff9b"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}