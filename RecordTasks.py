import asyncio
from recordGenerators import Alerts,CurrentObservations,HourlyForecast,DailyForecast, AirQuality, AirportDelays, AchesAndPains, Breathing, HeatingAndCooling, MosquitoActivity, PollenForecast, TideForecast, WateringNeeds
from radar import TWCRadarCollector


""" This houses the tasks needed to update the data records concurrently 
    I have no idea if this is a messy way to do things, but it will be worked upon if it is.
"""

async def alertsTask():
    while True:
        await Alerts.makeRecord()
        await asyncio.sleep(60)

async def coTask():
    while True:
        await CurrentObservations.makeDataFile()
        await asyncio.sleep(5 * 60)

# These tasks should be updated every hour

async def hfTask():
    while True:
        await HourlyForecast.makeDataFile()
        await asyncio.sleep(60 * 60)

async def dfTask():
    while True:
        await DailyForecast.makeDataFile()
        await asyncio.sleep(60 * 60)

async def aqTask():
    while True:
        await AirQuality.writeData()
        await asyncio.sleep(60 * 60)

async def aptTask():
    while True:
        await AirportDelays.writeData()
        await asyncio.sleep(60 * 60)

async def apTask():
    while True:
        await AchesAndPains.makeRecord()
        await asyncio.sleep(60 * 60)

async def brTask():
    while True:
        await Breathing.makeDataFile()
        await asyncio.sleep(60 * 60)

async def hcTask():
    while True:
        await HeatingAndCooling.makeRecord()
        await asyncio.sleep(60 * 60)

async def maTask():
    while True:
        await MosquitoActivity.makeRecord()
        await asyncio.sleep(60 * 60)

async def pTask():
    while True:
        await PollenForecast.makeDataFile()
        await asyncio.sleep(60 * 60)

async def tTask():
    while True:
        await TideForecast.makeRecord()
        await asyncio.sleep(60 * 60)

async def wnTask():
    while True:
        await WateringNeeds.makeRecord()
        await asyncio.sleep(60 * 60)