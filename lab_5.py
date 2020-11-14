from __future__ import print_function 
from pyspark.context import SparkContext
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql.session import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import PCA
from pyspark.ml.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.util import MLUtils
import numpy as np
from pyspark.ml.feature import StandardScaler
import pyspark.sql.functions as f
import pyspark.sql.types
from pyspark.sql import Row
from pyspark.sql.types import DoubleType
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import PCA 

sc = SparkContext()
spark = SparkSession(sc)

df = spark.read.format("bigquery").option("table", "lab5.iris").load().toDF("sl", "sw", "pl", "pw", "labclass")
data = df.withColumn("label", df["labclass"])
print('Read the Dataframe')


cols = df.drop('labclass').columns
print('Dropped the target label')

assembler = VectorAssembler(inputCols=cols, outputCol = 'features')
print('Assembled all the features into one single vector')
labelIndexer = StringIndexer(inputCol="labclass", outputCol="indexedLabel").fit(df)
print('The categorical label has been indexed with numerical data type')

scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures", withStd=False, withMean=True)
print(' The columns have been scaled')
pca = PCA(k=4, inputCol='scaledFeatures', outputCol='pcaFeature')
print('Applied PCA to the data')
(trainingData, testData) = df.randomSplit([0.7, 0.3])

rf = RandomForestClassifier(labelCol="indexedLabel", featuresCol="pcaFeature", numTrees=10)
print('Used Random Forest Ensemble')
labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel",
                               labels=labelIndexer.labels)
print('Convert the numerical label back into the datatype ')
pipeline = Pipeline(stages=[labelIndexer, assembler,scaler,pca, rf, labelConverter])
print('Created Pipeline')
model = pipeline.fit(trainingData)
print('Fitted Data')
predictions = model.transform(testData)
predictions.show(10)
print('Predictions have been printed')
evaluator = MulticlassClassificationEvaluator(
    labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
print('Evaluator Defined')
accuracy = evaluator.evaluate(predictions)
print("Test Error = %g" % (1.0 - accuracy))

from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="pcaFeature")
pipeline = Pipeline(stages=[labelIndexer, assembler,scaler,pca, dt, labelConverter])
print('Created Pipeline')
model = pipeline.fit(trainingData)
print('Fitted Data')
predictions = model.transform(testData)
predictions.show(10)
print('Predictions have been printed')
evaluator = MulticlassClassificationEvaluator(
    labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
print('Evaluator Defined')
accuracy = evaluator.evaluate(predictions)
print("Test Error = %g" % (1.0 - accuracy))




