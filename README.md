# Django Reviewing

[![Build Status](https://travis-ci.org/maykinmedia/djadyen.svg?branch=master)](https://travis-ci.org/maykinmedia/djadyen)
[![codecov](https://codecov.io/gh/maykinmedia/djadyen/branch/master/graph/badge.svg)](https://codecov.io/gh/maykinmedia/djadyen)
[![Lintly](https://lintly.com/gh/maykinmedia/djadyen/badge.svg)](https://lintly.com/gh/maykinmedia/djadyen/)
[![PyPI](https://img.shields.io/pypi/dm/Django.svg)](https://pypi.python.org/pypi/djadyen/0.1.7)
[![PyPI](https://img.shields.io/pypi/v/nine.svg)]([![PyPI](https://img.shields.io/pypi/dm/Django.svg)](https://pypi.python.org/pypi/djadyen/0.1.7))
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]([![PyPI](https://img.shields.io/pypi/v/nine.svg)]([![PyPI](https://img.shields.io/pypi/dm/Django.svg)](https://pypi.python.org/pypi/djadyen/0.1.7)))
[![PyPI](https://img.shields.io/pypi/l/Django.svg)]([![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]([![PyPI](https://img.shields.io/pypi/v/nine.svg)]([![PyPI](https://img.shields.io/pypi/dm/Django.svg)](https://pypi.python.org/pypi/djadyen/0.1.7))))

This module is used to connect your django application to the payment provider Adyen.
Before working with this module please also read the [documentation on Adyen](https://docs.adyen.com/developers/hpp-manual).

This is only tested on a postgres database.

## Installation

Install with pip
```shell
pip install django-reviewing
```

Add *'adyen'* to the installed apps
```python
# settings.py

INSTALLED_APPS = [
    ...
    'reviews',
    ...
]
```

Add the Adyen notifications urls (This is not required). These url will save all the notifications to the database. You need to make an implementation to handle the notifications
```python
# urls.py

urlpatterns = [
    ...
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    ...
]
```

## Settings

There are several settings which you can use within settings.py:

```python
    REVIEWS_IS_MODERATED = False
    # If True the admin has to publish a review manually. Otherwise a review is
    public right after it has been added.

    REVIEWS_SHOW_PREVIEW = False
    # If True a preview is displayed to the user before he can submit the review.

    REVIEWS_IS_EMAIL_REQUIRED = False
    # If True the e-mail field of the review is mandatory. (if the user is anonymous)

    REVIEWS_IS_NAME_REQUIRED = False
    # If True the name field of the review is mandatory. (if the user is anonymous)
```

## Usage

Add the provided tags to your templates

```html
    {% load reviews_tags %}

    <html>
        <head>
            <title>{{ flatpage.title }}</title>
        </head>
        <body>
            {{ flatpage.content }}
            {% average_for_instance flatpage %}

            <hr>
            {% reviews_for_instance flatpage %}

        </body>
    </html>
```

## Example

There is a simple example provided with this product.

To install it just make sure *django.contrib.flatpages* has been installed (a
flatpage will serve as our test content) and add reviews.example to
*INSTALLED_APPS*.

Now add a flatpage and browse to it. You should be able to add reviews to the
flatpage now.
