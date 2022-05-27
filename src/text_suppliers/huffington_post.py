from typing import Optional
from .text_suppliers import TextSupplier
import requests
from lxml import etree

IGNORE_URLS = {
    "https://www.huffingtonpost.co.uk/news/covid-health-questions/",
    "https://www.nhs.uk/conditions/coronavirus-covid-19/",
}
IGNORE_TAGS_IN_TEXT = {
    "a",
    "b",
    "i",
    "span",
    "ul",
    "li",
    "p",
    "em",
    "h2",
    "h3",
    "div",
    "strong",
}

class HuffingtonPostTextSupplier(TextSupplier):
    """Downlaods latest article from huffingtonpost.co.uk"""

    def __init__(self, url: Optional[str] = None, hf_tag: Optional[str] = None) -> None:
        self.url = url
        self.base_url = "https://www.huffingtonpost.co.uk/news"
        if hf_tag is not None:
            self.base_url += "/" + hf_tag
        super().__init__

    def _get_latest_new_link(self) -> str:
        title_xpath = """//a[contains(@class, 'card__headline')]"""

        html = requests.get(self.base_url).text
        tree = etree.HTML(html)
        titles = tree.xpath(title_xpath)
        article_links = []
        for tit in titles:
            link = tit.attrib["href"]
            if link not in IGNORE_URLS:
                article_links.append(link)
        return article_links[0]

    def _get_text_from_news_page(self, url: str) -> str:
        paragraph_xpath = """//div[contains(@class, 'cli-text') and contains(@class, 'primary-cli')]"""
        paragraph2_xpath = """//div[@class='content-list-component text']"""

        resp = requests.get(url)
        pagehtml = resp.text
        tree = etree.HTML(pagehtml)

        paragraphs = tree.xpath(paragraph_xpath)
        if len(paragraphs) == 0:
            paragraphs = tree.xpath(paragraph2_xpath)
        text = ""
        for par in paragraphs:
            etree.strip_tags(par, IGNORE_TAGS_IN_TEXT)
            if par.text is not None:
                text += par.text + "\n"
        return text

    def get_all_texts(self) -> str:
        url = self.url
        if url is None:
            url = self._get_latest_new_link()
        text = self._get_text_from_news_page(url)
        return [text]
