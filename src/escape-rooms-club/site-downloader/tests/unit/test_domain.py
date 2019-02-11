from . import fakes

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

from domain import SiteDownloader


def test_site_downloader_success():
    site_url = "https://www.test-website.com"
    file_content = "This is test website content which should be download"
    
    web_client = fakes.FakeWebClient({
        site_url: file_content
    })
    storage_client = fakes.FakeStorageClient()

    site_downloader = SiteDownloader(web_client, storage_client)
    success, error_message = site_downloader.download_site_and_store_its_content(site_url, "bucket_name", "test-website.com")

    assert success is True, "Operation should have succeeded"
    assert not error_message, "Error message should be none"

    files_for_bucket = storage_client.files["bucket_name"]
    assert files_for_bucket
    
    file_key = files_for_bucket[file_content]
    assert file_key.startswith("test-website.com/")


def test_site_downloader_web_client_failure():
    site_url = "http://www.site.com"
    site_downloader = SiteDownloader(fakes.FakeWebClientBroken(), fakes.FakeStorageClient())
    success, error_message = site_downloader.download_site_and_store_its_content(
        site_url, 
        "bucket_name", 
        "test-website.com")

    assert success is False, "Operation should have failed"
    assert error_message == f"Request to a site_url: {site_url} has failed", "Error message should not be none"


def test_site_downloader_storage_client_failure():
    site_url = "https://www.test-website.com"
    file_content = "This is test website content which should be download"
    
    web_client = fakes.FakeWebClient({
        site_url: file_content
    })

    site_downloader = SiteDownloader(web_client, fakes.FakeStorageClientBroken())
    success, error_message = site_downloader.download_site_and_store_its_content(
        site_url, 
        "bucket_name", 
        "test-website.com")

    assert success is False, "Operation should have failed"
    assert error_message == f"Request to a file upload has failed", "Error message should not be none"
