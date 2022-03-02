# Game-Recommendation

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
This algorithm recommends games based on user Steam library.

## Technologies
Pandas and numpy for data modification.

Collaborative Filtering based on Item similarity:
* Cosine_similarity from sklearn <br />

Collaborative Filtering based on User similarity:
* Pearsonr algorithm from scipy.stats <br />

For gathering data from Steam
*  Many thanks to [zeo's](https://github.com/zeo/python-steamuser) steam project<br />

## Setup
To run this project, paste Your steam Id and steam API key [here](https://github.com/Medokins/Game-Recommendation/blob/main/SteamAPI/steamUserData.py).
* [steam API Key](https://steamcommunity.com/dev/apikey) <br />
* [steam Id](https://www.youtube.com/watch?v=wuvE6XDs3WQ&ab_channel=AKInformatica-AkEsports-EsportPalace) (It's a 40s video, this wasn't created by me) 