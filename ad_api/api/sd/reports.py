from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Reports(Client):
    """Sponsored Display Reports
    
    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-display/3-0/openapi#/
    
    The Sponsored Display API supports creation of reports for campaigns, ad groups, product ads, targets, and asins. Create a ReportRequest object specifying the fields corresponding to performance data metrics to include in the report. See ReportRequest object for more information about the performance data metric fields and their descriptions.
    """
    
    @sp_endpoint('/sd/{}/report', method='POST')
    def post_report(self, recordType, **kwargs) -> ApiResponse:
        r"""Requests a Sponsored Display report.

        Request the creation of a performance report for all entities of a
        single type which have performance data to report. Record types can be
        one of campaigns, adGroups, keywords, productAds, asins, and targets.
        Note that for asin reports, the report currently can not include metrics
        associated with both keywords and targets. If the targetingId value is
        set in the request, the report filters on targets and does not return
        sales associated with keywords. If the targetingId value is not set in
        the request, the report filters on keywords and does not return sales
        associated with targets. Therefore, the default behavior filters the
        report on keywords. Also note that if both keywordId and targetingId
        values are passed, the report filters on targets only and does not
        return keywords.

        Keyword Args
            | path **recordType** (string): The type of entity for which the report should be generated. Available values : campaigns, adGroups, productAds, targets, asins [required]

        Request body
            | **reportDate** (string): [optional] The date for which to retrieve the performance report in YYYYMMDD format. The time zone is specified by the profile used to request the report. If this date is today, then the performance report may contain partial information. Reports are not available for data older than 60 days. For details on data latency, see the Service Guarantees in the developer notes section.
            | **tactic** (string): [optional] The advertising tactic associated with the campaign. The following table lists available tactic names: T00001, T00020, T00030, remarketing
            | **metrics** (string) [optional] A comma-separated list of the metrics to be included in the report. The following tables summarize report metrics which can be requested via the reports interface. Different report types can use different metrics. Note that ASIN reports only return data for either keywords or targets, but not both.
        
        Returns:
            ApiResponse
        
        """
        return self._request(fill_query_params(kwargs.pop('path'), recordType), data=kwargs.pop('body'), params=kwargs)
    
    @sp_endpoint('/v2/reports/{}', method='GET')
    def get_report(self, reportId, **kwargs) -> ApiResponse:
        r"""Gets a previously requested report specified by identifier.

        Keyword Args
            | path **reportId** (string): [required] The report identifier.

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)
    
    def download_report(self, **kwargs) -> ApiResponse:
        r"""Downloads the report previously get report specified by location
        (this is not part of the official Amazon Advertising API, is a helper
        method to download the report). Take in mind that a direct download of
        location returned in get_report will return 401 - Unauthorized.

        kwarg parameter **file** if not provided will take the default amazon
        name from path download (add a path with slash / if you want a specific
        folder, do not add extension as the return will provide the right
        extension based on format choosed if needed)

        kwarg parameter **format** if not provided a format will return a url
        to download the report (this url has a expiration time)

        Keyword Args
            | **url** (string): [required] The location obatined from get_report
            | **file** (string): [optional] The path to save the file if mode is download `json`, `zip` or `gzip`.
            | **format** (string): [optional] The mode to download the report: `data` (list), `raw`, `url`, `json`, `zip`, `gzip`. Default (`url`)

        Returns:
            ApiResponse
        """
        return self._download(self, params=kwargs)
