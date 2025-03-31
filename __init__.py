import os
from google import genai
from google.genai import types
import re
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv