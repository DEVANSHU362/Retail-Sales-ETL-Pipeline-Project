# Databricks notebook source
df = spark.read.csv("/Volumes/workspace/default/project2/customers.csv", header=True, inferSchema=True)

df1 = spark.read.csv("/Volumes/workspace/default/project2/orders.csv" ,header =True ,inferSchema=True)

df2 = spark.read.csv("/Volumes/workspace/default/project2/products.csv" ,header =True ,inferSchema=True)

df3 = spark.read.csv("/Volumes/workspace/default/project2/stores.csv" ,header =True ,inferSchema=True)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df.printSchema()
df1.printSchema()
df2.printSchema()
df3.printSchema()

# COMMAND ----------

df = df.fillna('Not_Available')
df = df.fillna(0)
df1 = df1.fillna('Not_Available')
df1 = df1.fillna(0)
df2 = df2.fillna('Not_Available')
df2 = df2.fillna(0)
df3 = df3.fillna('Not_Available')
df3 = df3.fillna(0)

# COMMAND ----------

df.count()
df1.count()
df2.count()
df3.count()

# COMMAND ----------


df = df.dropDuplicates(subset = ['Customer_ID'])
df1 = df1.dropDuplicates(subset = ['Order_ID'])
df2 = df2.dropDuplicates(subset = ['Product_ID'])
df3 = df3.dropDuplicates(subset = ['Store_ID'])

df.printSchema()
df1.printSchema()
df2.printSchema()
df3.printSchema()

df.count()
df1.count()
df2.count()
df3.count()

# COMMAND ----------

df = df.withColumnRenamed('City','Customer_City')
df = df.withColumnRenamed('State','Customer_State')

# COMMAND ----------

from pyspark.sql.functions import *
df.filter(col('Customer_ID').isNull()).count()
df1.filter(col('Order_ID').isNull()).count()
df2.filter(col('Product_ID').isNull()).count()
df3.filter(col('Store_ID').isNull()).count()

# COMMAND ----------

from pyspark.sql.functions import *
final_DataFrame = (
    df1
    .join(df ,df1.Customer_ID == df.Customer_ID,'left')
    .join(df2 ,df1.Product_ID == df2.Product_ID,'left')
    .join(df3 ,df1.Store_ID == df3.Store_ID,'left')
)

display(final_DataFrame)

# COMMAND ----------

display(final_DataFrame)

# COMMAND ----------

final_DataFrame = final_DataFrame.drop(df.Customer_ID)
final_DataFrame = final_DataFrame.drop(df2.Product_ID)
final_DataFrame = final_DataFrame.drop(df3.Store_ID)
display(final_DataFrame)


# COMMAND ----------

from pyspark.sql.functions import *
for column in final_DataFrame.columns:
     is_null = final_DataFrame.filter(col(column).isNull()).count()
print(is_null)

# COMMAND ----------

from pyspark.sql.functions import *
final_DataFrame = final_DataFrame.withColumn('Total_Amount' , col('Quantity')*col('Price'))
final_DataFrame = final_DataFrame.withColumn('Final_Amount' , col('Total_Amount') - col('Discount'))
display(final_DataFrame)

# COMMAND ----------

final_DataFrame = final_DataFrame.withColumn('Order_Year' , year('Order_Date'))
final_DataFrame = final_DataFrame.withColumn('Order_Month' , month('Order_Date'))
final_DataFrame = final_DataFrame.withColumn('Order_Day' , dayofmonth('Order_Date'))
display(final_DataFrame)

# COMMAND ----------

from pyspark.sql.functions import *
for column in final_DataFrame.columns:
    is_null = final_DataFrame.filter(col(column).isNull()).count()
    print(f"{column}: {is_null}")

# COMMAND ----------

final_DataFrame.write \
    .format("mysql") \
    .option("host", "mysql-2b189533-devanshujangid160-3f16.d.aivencloud.com") \
    .option("port", "13779") \
    .option("database", "defaultdb") \
    .option("dbtable", "retail_sales") \
    .option("user", "avnadmin") \
    .option("password", "**********") \
    .option("requireSSL", "true") \
    .mode("append") \
    .save()