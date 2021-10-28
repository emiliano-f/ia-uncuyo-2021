## Funcion create_folds

create_folds <- function(dataframe, n){

  rows = nrow(dataframe)

  data_partition <- ceiling(rows/n)

  datasplit <- split(dataframe, sample(rep(1:n, data_partition))) #return list

  print(datasplit)

  return(datasplit)
}
