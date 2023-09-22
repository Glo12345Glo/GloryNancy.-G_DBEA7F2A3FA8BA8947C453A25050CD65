#Write a function called linear_search_product that takes the list of products and a target product name as input. 

def linear_search_product(productList, targetProduct):
  indices=[]
  for index, product in enumerate(productList):
    if product==targetProduct:
      indices.append(index)
  return indices

#Example usage:
products=["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target="sandal"
result=linear_search_product(products, target)
print(result)
