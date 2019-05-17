from __future__ import absolute_import, print_function, unicode_literals

import os

from openweathermap_requests import OpenWeatherMapRequests

import utils


class OpenWeatherMap(object):

    SOMETHING = utils.GlobalUtils()
    OWM_CONFIG = SOMETHING.full_config["openweathermap"]
    OWM_CACHE = os.path.join(SOMETHING.current_location, "../data/owm_cache")
    LON, LAT = OWM_CONFIG["lon"], OWM_CONFIG["lat"]

    OW = OpenWeatherMapRequests(
        api_key=OWM_CONFIG["api_key"],
        cache_name=OWM_CACHE,
        expire_after=5 * 60,
    )

    LOGGER = SOMETHING.handler

    @classmethod
    def get_current_weather(cls):
        """
        Grabs the current weather.

        Args:
          None
        Returns:
          A dict with the results of the weather query.
        """
        OpenWeatherMap.LOGGER.debug("Grabbing the current weather.")
        resp = OpenWeatherMap.OW.get_weather(
            lon=OpenWeatherMap.LON, lat=OpenWeatherMap.LAT
        )
        OpenWeatherMap.LOGGER.debug("Weather success! Results: %s", resp)
        return resp


if __name__ == "__main__":
    OWM = OpenWeatherMap()
    print(OWM.get_current_weather())
