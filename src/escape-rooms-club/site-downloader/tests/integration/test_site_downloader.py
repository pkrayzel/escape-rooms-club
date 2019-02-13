import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

from domain import SiteDownloader
from dao import WebClient, StorageClient


def test_site_downloader_success():
    storage_client = StorageClient(endpoint_url="http://localstack:4572")
    site_downloader = SiteDownloader(WebClient(), storage_client)

    bucket_name = "scrapers-output"
    target_directory = "exitgames.cz"
    success, error_message = site_downloader.download_site_and_store_its_content(
        site_url="http://website:5000/exitgames.cz", 
        bucket_name=bucket_name, 
        target_directory=target_directory
    )

    assert success is True, "Operation should have succeeded"
    assert not error_message, "Error message should be none"

    file_keys = storage_client.find_all_file_keys_in_directory(
        bucket_name=bucket_name, 
        directory=target_directory
    )
    # we expect the last found file to be the one created during this test
    last_file_content = storage_client.get(
        bucket_name=bucket_name, 
        file_key=file_keys[-1])
    
    assert 'href="https://www.exitgames.cz/seznam-unikovych-her"' in last_file_content.decode('UTF-8')


def test_site_downloader_web_client_failure():
    storage_client = StorageClient(endpoint_url="http://localstack:4572")
    site_downloader = SiteDownloader(WebClient(), storage_client)

    site_url = "http://website:5000/not-existing-site.cz"
    bucket_name = "scrapers-output"
    target_directory = "not-existing-site.cz"

    success, error_message = site_downloader.download_site_and_store_its_content(
        site_url=site_url, 
        bucket_name=bucket_name, 
        target_directory=target_directory
    )

    assert success is False, "Operation should have failed"
    assert site_url in error_message, "Error message should not be none and should contain site_url"


def test_site_downloader_storage_client_failure():
    storage_client = StorageClient(endpoint_url="http://localstack:4572")
    site_downloader = SiteDownloader(WebClient(), storage_client)

    site_url = "http://website:5000/exitgames.cz"
    bucket_name = "not-existing-bucket"
    target_directory = "exitgames.cz"

    success, error_message = site_downloader.download_site_and_store_its_content(
        site_url=site_url, 
        bucket_name=bucket_name, 
        target_directory=target_directory
    )

    assert success is False, "Operation should have failed"
    assert 'The specified bucket does not exist' in error_message, "Error message should not be none"
