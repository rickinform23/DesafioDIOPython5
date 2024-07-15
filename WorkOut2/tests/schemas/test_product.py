from uuid import UUID
from store.schemas.product import ProductIn

from pydantic import ValidationError
import pytest
from tests.factories import product_data


def test_schemas_sucess():
    data = product_data()
    product = ProductIn.model_validate(data)
    
    assert product.name == "Iphone 14 pro Max"
    


def test_schemas_return_raise():
    data = {"name":"Iphone 14 pro Max", "quantity": 10, "price": 8.500}
    
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)
    
    assert err.value.errors()[0] == {}
    
    
    
    