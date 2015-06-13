import requests, xmltodict

class Api(object):
    def __init__(self, domain, affiliate_id, api_key):
        self.domain = domain
        self.affid = affiliate_id
        self.api_key = api_key
        self.headers = {'User-Agent': 'cake.py 0.1'}

    def offer_feed(self, **kwargs):
        url = 'http://{0}/affiliates/api/4/offers.asmx/OfferFeed'.format(self.domain)
        defaults = dict(
            api_key=self.api_key,
            affiliate_id=self.affid,
            campaign_name='',
            vertical_category_id=0,
            media_type_category_id=0,
            vertical_id=0,
            offer_status_id=0,
            tag_id=0,
            start_at_row=1,
            row_limit=0
        )

        defaults.update(kwargs)

        result = requests.get(url, params=defaults, headers=self.headers)

        d = xmltodict.parse(result.text)

        return d['offer_feed_response']['offers']['offer']

    def get_suppression_list(self, offer_id, **kwargs):
        url = 'http://{0}/affiliates/api/2/offers.asmx/GetSuppressionList'.format(self.domain)
        defaults = dict(
            api_key=self.api_key,
            affiliate_id=self.affid,
            offer_id=offer_id,
        )
        defaults.update(kwargs)

        result = requests.get(url, params=defaults, headers=self.headers)

        d = xmltodict.parse(result.text)

        return d['suppression_list_response']['download_url']

    def get_campaign(self, campaign_id, **kwargs):
        url = 'http://{0}/affiliates/api/2/offers.asmx/GetCampaign'.format(self.domain)
        defaults = dict(
            api_key=self.api_key,
            affiliate_id=self.affid,
            campaign_id=campaign_id,
        )
        defaults.update(kwargs)

        result = requests.get(url, params=defaults, headers=self.headers)

        d = xmltodict.parse(result.text)

        return d['campaign_response']['campaign']

    def get_creative_code(self, campaign_id, creative_id, **kwargs):
        url = 'http://{0}/affiliates/api/2/offers.asmx/GetCreativeCode'.format(self.domain)
        defaults = dict(
            api_key=self.api_key,
            affiliate_id=self.affid,
            campaign_id=campaign_id,
            creative_id=creative_id,
        )
        defaults.update(kwargs)

        result = requests.get(url, params=defaults, headers=self.headers)

        d = xmltodict.parse(result.text)

        if d['creative_code_response']['creative_files']:
            return d['creative_code_response']['creative_files']['creative_file']
        else:
            return {u'file_content':u'', u'file_name':u''}
