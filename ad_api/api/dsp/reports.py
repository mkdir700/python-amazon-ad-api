from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Reports(Client):
    """DSP Reports
    
    Documentation: https://advertising.amazon.com/API/docs/en-us/dsp-reports-beta-3p/#/Reports
    
    """
    
    @sp_endpoint('/dsp/reports', method='POST')
    def post_report(self, **kwargs) -> ApiResponse:
        r"""Requests a DSP report.

        Use this operation to request creation of a report that includes metrics about your Amazon DSP campaigns.

        Request body
            | **advertiserIds** (list): [optional] Advertiser ID list.
            | **endDate** (string): [required] Date in `YYYYMMDD` format. The report contains only metrics generated on the specified date range between startDate and endDate. The maximum date range between startDate and endDate is 31 days. The endDate can be up to 90 days older from today.
            | **format** (string): [optional] Available values: `JSON`(default), `CSV`. The report file format.
            | **orderIds** (list): [optional] Order ID list.
            | **metrics** (string): [optional] Specify a comma-delimited string of metrics field names to include in the report. For example: "impressions, clickThroughs, CTR, eCPC, totalCost, eCPM". If no metric field names are specified, only the default fields and selected DIMENSION fields are included by default. Specifying default fields returns an error.
            | **type** (string): [optional] Available values: `CAMPAIGN`(default), `INVENTORY`, `AUDIENCE`, `PRODUCTS`, `TECHNOLOGY`, `GEOGRAPHY`. The report type.
            | **startDate** (string): [optional] Date in `YYYYMMDD` format. The report contains only metrics generated on the specified date range between startDate and endDate. The maximum date range between startDate and endDate is 31 days. The startDate can be up to 90 days older from today.
            | **dimensions** (list): [optional] List of dimensions to include in the report. Specify one or many comma-delimited strings of dimensions. For example: ["ORDER", "LINE_ITEM", "CREATIVE"]. Adding a dimension in this array determines the aggregation level of the report data and also adds the fields for that dimension in the report. If the list is null or empty, the aggregation of the report data is at ORDER level. The allowed values can be used together in this array as an allowed value in which case the report aggregation will be at the lowest aggregation level and the report will contain the fields for all the dimensions included in the report.
            | **timeUnit** (string): [optional] Available values: `DAILY`, `SUMMARY`(default). Adding timeUnit determines the aggregation level (SUMMARY or DAILY) of the report data. If the timeUnit is null or empty, the aggregation of the report data is at the SUMMARY level and aggregated at the time period specified. DAILY timeUnit is not supported for AUDIENCE report type.
            
        Returns:
            ApiResponse

        """
    
    @sp_endpoint('/dsp/reports/{}', method='GET')
    def get_report(self, reportId, **kwargs) -> ApiResponse:
        r"""Gets a previously requested report specified by identifier.
        
        Pass the identifier of a previously requested report in the reportId field to get the current status of the report. While the report is pending, status is set to `IN_PROGRESS`. When a reponse with status set to `SUCCESS` is returned, the report is available for download at the address specified in the location field.
        
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
            | **url** (string): [required] The location obatined from get_report.
            | **file** (string): [optional] The path to save the file if mode is download `json`, `zip` or `gzip`.
            | **format** (string): [optional] The mode to download the report: `data` (list), `raw`, `url`, `json`, `zip`, `gzip`. Default (`url`)

        Returns:
            ApiResponse
        """
        return self._download(self, params=kwargs)
