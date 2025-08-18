/*
df= df.filter( (df.course=="Db")&(df.marks>=50)  ).show()

courses=["DB","Cloud","OOP","DSA"];

df.filter(df.course.isin(courses)).show();

df.filter(df.courses.startsWith("D")).show();

df.name.endswith("E")

df.filter(df.name.like('%se%'));


Quiz

create a new column 120 
all student with more than 80% marks

withColumn to create a new column 


df=df.withColumn("totalColumn",lit(120));
df=df.withColumn("average",col("marks")/col("total_marks")*100).show();


df.filter( (df.course=="OOP") &(df.average>80) )


COUNT,DISTINCT,DROPDUPLICATES

df.count()  //rows

show and count is an action
only one can be used


df.filter(db.course=="DB").count();


unique rows age gender and course withColumn

df.select("age","gender","course").distinct()

using drop DROPDUPLICATES
df.DROPDUPLICATES("age","gender","course");



Spark DF (sort and orderBy)

// we can use interchangibly 
df.sort("marks","age").show()
df.sort(df.marks,df.age).show()


df.orderBy("marks","age").show()
df.orderBy(df.marks.asc(),df.age.desc()).show()


df.sort(df.bonus.asc()).show()

df.sort(df.age.asc(),df.salary.desc()).show()

df.sort(df.bonus.desc(),df.age.desc(),df.salary.asc()).show()












*/