from celery import shared_task
from aiproduct.apps.product.models import Product, ProductClick


@shared_task
def process_product_click_events(product_id, uid, click_source):
    product = Product.objects.get(pk=product_id)
    filter_kwargs = {'uid': uid}
    has_clicked_product = ProductClick.objects.filter(
        product=product,
        **filter_kwargs,
    ).exists()
    if not has_clicked_product:
        ProductClick.objects.create(
            uid=uid,
            click_source=click_source,
            product=product,
        )


@shared_task
def scrape_and_insert_ai_product_data():
    # Add your scraping logic here.

    # Once you fetch data, you can insert it into the database. An example is provided below.

    product_data = []  # Your own function
    for product in product_data:
        Product.objects.create(
            title=product['title'],
            url=product['url'],
            image_url=product['image_url'],
            description=product['description'],
            category=product['category']
        )