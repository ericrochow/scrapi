from __future__ import absolute_import, unicode_literals

import fitbit

import utils


class FitbitData(object):

    SOMETHING = utils.GlobalUtils()
    FITBIT_CONFIG = SOMETHING.full_config["fitbit"]
    FITBIT = fitbit.Fitbit(
        FITBIT_CONFIG["consumer_key"],
        FITBIT_CONFIG["consumer_secret"],
        FITBIT_CONFIG["access_token"],
        FITBIT_CONFIG["refresh_token"],
    )

    @classmethod
    def body_data_log(cls):
        """
        """
        return FitbitData.FITBIT.body()

    @classmethod
    def activity_log(cls):
        """
        """
        return FitbitData.FITBIT.activities()

    @classmethod
    def food_log(cls):
        """
        """
        return FitbitData.FITBIT.foods_log()

    @classmethod
    def sleep_log(cls):
        """
        """
        return FitbitData.FITBIT.sleep()

    @classmethod
    def heart_log(cls):
        """
        """
        return FitbitData.FITBIT.heart()
