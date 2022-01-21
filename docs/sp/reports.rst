Reports
=======

.. autoclass:: ad_api.api.sp.Reports

    .. autofunction:: ad_api.api.sp.Reports.post_report(self, recordType, **kwargs) -> ApiResponse:

        ### Example python

        .. code-block:: python

            from ad_api.api.sp.reports import Reports

            file = open("ad_groups.json")
            data = file.read()
            file.close()

            # Available values : campaigns, adGroups, keywords, productAds, asins, targets
            record_type = 'adGroups'

            result = Reports().post_report(
                recordType=record_type,
                body=data
            )

            payload = result.payload
            report_id = payload.get('reportId')

        ### Example json

        Open this :download:`json <../../test/reports/sp-sx-ad_groups-report.json>` file to see the result:

        .. literalinclude:: ../../test/reports/sp-sx-ad_groups-report.json


    .. autofunction:: ad_api.api.sp.Reports.get_report(self, reportId, **kwargs) -> ApiResponse:

        ### Example python

        .. code-block:: python

            from ad_api.api.sp.reports import Reports

            # this report_id is obtained from post_report method
            report_id = 'amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c'

            result = Reports().get_report(
                reportId=report_id
            )

        ### Result json

        .. sourcecode:: json

            {
                "expiration": 1640736000000,
                "fileSize": 6546,
                "location": "https://advertising-api-eu.amazon.com/v1/reports/amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c/download",
                "reportId": "amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c",
                "status": "SUCCESS",
                "statusDetails": "Report has been successfully generated."
            }


    .. autofunction:: ad_api.api.sp.Reports.download_report(self, **kwargs) -> ApiResponse:

        .. warning::

            This method is not a part of the Amazon Advertising Api.

        ### Example python

        .. code-block:: python

            from ad_api.api.sp.reports import Reports

            # the url=location is obtained from get_report method need to in stay 'status': 'SUCCESS' if is 'IN_PROGRESS' the report cannot be downloaded
            location = 'https://advertising-api-eu.amazon.com/v1/reports/amzn1.clicksAPI.v1.p44551.61549C5E.e4599469-7392-4624-a858-fc1fecdb165c/download'

            # path = '/Users/your-profile/Downloads/report_name'
            # mode = "data"  # "data (list), raw, url, json, zip, gzip default is url"

            result = Reports().download_report(
                url=location,
                # file=path,
                # format=mode
            )


        .. tip::

           Just provide the url keyword arg with the location and you will get a response with the url ready to download
