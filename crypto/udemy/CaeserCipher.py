{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled14.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyM8sCRD67qrvT6hFlUeRaGd",
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
        "<a href=\"https://colab.research.google.com/github/davidzheng66/python3/blob/master/crypto/udemy/CaeserCipher.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ilFIXTTac-in",
        "outputId": "46e60ce5-beb8-4aee-c333-1e76e571f9ae"
      },
      "source": [
        "def generate_key(n):\n",
        "    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\n",
        "    key = {}\n",
        "    cnt = 0\n",
        "    for c in letters:\n",
        "        key[c] = letters[(cnt + n) % len(letters)]\n",
        "        cnt += 1\n",
        "    return key\n",
        "\n",
        "def get_decryption_key(key):\n",
        "    dkey = {}\n",
        "    for c in key:        \n",
        "        dkey[key[c]] = c\n",
        "    return dkey\n",
        "\n",
        "def encrypt(key, message):\n",
        "    cipher = ''\n",
        "    for c in message:\n",
        "        if c in key:\n",
        "            cipher += key[c]\n",
        "        else:\n",
        "            cipher += c\n",
        "    return cipher\n",
        "\n",
        "key = generate_key(3)\n",
        "print(\"Key: \\n\", key)\n",
        "\n",
        "dkey = get_decryption_key(key)\n",
        "print('dkey: \\n', dkey)\n",
        "\n",
        "message = \"YOU ARE AWESOME1\"\n",
        "print('message: ', message)\n",
        "\n",
        "cipher = encrypt(key, message)\n",
        "print(\"cipher: \", cipher)\n",
        "\n",
        "# dkey = generate_key(26-3)\n",
        "# print('dkey: ', dkey)\n",
        "\n",
        "message = encrypt(dkey, cipher)\n",
        "print(\"message: \", message)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Key: \n",
            " {'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'}\n",
            "dkey: \n",
            " {'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W', 'A': 'X', 'B': 'Y', 'C': 'Z'}\n",
            "message:  YOU ARE AWESOME1\n",
            "cipher:  BRX DUH DZHVRPH1\n",
            "message:  YOU ARE AWESOME1\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}