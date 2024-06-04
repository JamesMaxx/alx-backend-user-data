# README

## Table of Contents

1. [Introduction](#introduction)
2. [What Is PII, Non-PII, and Personal Data?](#what-is-pii-non-pii-and-personal-data)
3. [Logging Documentation](#logging-documentation)
    - [Logging to Files](#logging-to-files)
    - [Setting Levels](#setting-levels)
    - [Formatting](#formatting)
4. [bcrypt Package](#bcrypt-package)
5. [Examples](#examples)

## Introduction

This README provides detailed information on Personally Identifiable Information (PII), non-PII, and personal data. It also covers logging practices, including logging to files, setting levels, and formatting. Additionally, it introduces the `bcrypt` package for hashing passwords.

## What Is PII, Non-PII, and Personal Data?

### PII (Personally Identifiable Information)

PII refers to information that can be used to identify an individual. Examples include:

- Full name
- Social Security number
- Email address
- Phone number
- Home address

### Non-PII (Non-Personally Identifiable Information)

Non-PII refers to data that cannot be used on its own to identify an individual. Examples include:

- Aggregated data
- Anonymized data
- Device types
- Browser types

### Personal Data

Personal data is any information that relates to an identified or identifiable individual. It encompasses both PII and non-PII. Examples include:

- IP addresses
- Cookies
- Behavioral data

## Logging Documentation

### Logging to Files

Logging to files involves writing log messages to a file on the disk. This is useful for keeping a record of events and diagnosing issues.

#### Example (Python)

```python
import logging

logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO)
logging.info('This is an info message')
