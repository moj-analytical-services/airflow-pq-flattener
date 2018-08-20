import sys

from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


args = getResolvedOptions(sys.argv, ["JOB_NAME", "source_path", "dest_path"])

print("args = ", args)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Body of the job
df = spark.read.json(args["source_path"])

columns = [
    df.tablingMemberPrinted[0]._value.alias("questionMP"),
    df.questionText,
    df.uin.alias("questionID"),
    df.tablingMemberConstituency._value.alias("MPConstituency"),
    df.date._value.alias("questionDate"),
    df.answer.answerText._value.alias("answerText"),
    df.answer.answeringMemberPrinted._value.alias("answerMP"),
    df.answer.dateOfAnswer._value.alias("answerDate"),
    df.AnsweringBody[0]._value.alias("answeringBody"),
]

df.select(columns).coalesce(1).write.csv(args["dest_path"], header=True)

job.commit()
