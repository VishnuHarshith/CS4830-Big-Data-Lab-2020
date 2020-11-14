import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions
options = PipelineOptions()
google_cloud_options = options .view_as(GoogleCloudOptions)
google_cloud_options.project = 'fit-assest-266717' 
google_cloud_options.job_name = 'lab3'
google_cloud_options.temp_location = "gs://mm16b009/tmp" 
options.view_as(StandardOptions).runner = 'DataflowRunner'
p = beam.Pipeline( options = options )
lines = p | 'Read' >> beam.io.ReadFromText( 'gs://iitm/files/file.txt' ) |
'Count' >> beam.combiners.Count.Globally(sum)
|'Write' >> beam.io.WriteToText( 'gs://mm16b009/outputs/' )
result = p.run()
