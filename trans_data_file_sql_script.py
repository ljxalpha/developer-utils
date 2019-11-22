#coding=utf-8
class SQLTransUtils():
#将数据文件转换成用于插入数据的sql文件
#dataFilePath：数据文件的绝对路径
#SQLScriptPath:SQL文件的输出路径
#tableName:数据库表名
#insertColumnNameDict:字典，用来表示取数据文件中的哪几列来插入数据表，每一列对应的字段名是什么
#insertColumnIsStrDict：字典，用来表示要插入数据表中的数据文件的列是不是字符串类型
#hasTitleLine:数据文件有没有标题行
#separator:每一行的分隔符
    def transDataFileToInsertSQLScript(self, dataFilePath,SQLScriptPath, tableName, insertColumnNameDict, insertColumnIsStrDict, hasTitleLine = True, separator = ","):
        dataFile = open(dataFilePath, "r")
        sourceData = dataFile.readlines()
        dataFile.close()
        if(hasTitleLine):
            sourceData = sourceData[1:]
        SQLScriptLines = []
        targetIndexList = insertColumnNameDict.keys()
        SQLHead = "insert into " + tableName + "("
        for index in targetIndexList:
            SQLHead = SQLHead + insertColumnNameDict[index] + ","
        SQLHead = SQLHead[:-1] + ") values "
        for sd in sourceData:
            row = sd
            if(sd[-1] == "\n"):
                row = sd[:-1]
            rowList = row.split(separator)
            SQLTail = "("
            for index in targetIndexList:
                if(insertColumnIsStrDict[index]):
                    SQLTail = SQLTail + "\"" + rowList[index] + "\"" + ","
                else:
                    SQLTail = SQLTail  + rowList[index]  + ","
            SQLTail = SQLTail + ");\n"
            SQL = SQLHead + SQLTail
            SQLScriptLines.append(SQL)

        SQLFile = open(SQLScriptPath, "w")
        SQLFile.writelines(SQLScriptLines)
        SQLFile.close()
        
#将数据文件转换成用于更新数据的sql文件
#dataFilePath：数据文件的绝对路径
#SQLScriptPath:SQL文件的输出路径
#tableName:数据库表名
#conditionColumnNameDict:字典，插入条件是数据文件的哪几列，每一列对应的字段名
#conditionColumnIsStrDict：字典，用来表示数据文件中的条件列都是不是字符串
#updateColumnNameDict:字典，用来表示取数据文件中的哪几列来插入数据表，每一列对应的字段名是什么
#updateColumnIsStrDict：字典，用来表示要插入数据表中的数据文件的列是不是字符串类型
#hasTitleLine:数据文件有没有标题行
#separator:每一行的分隔符
    def transDataFileToUpdateSQLScript(self, dataFilePath,SQLScriptPath, tableName, conditionColumnNameDict, conditionColumnIsStrDict, updateColumnNameDict, updateColumnIsStrDict,  hasTitleLine = True, separator = ","):
        dataFile = open(dataFilePath, "r")
        sourceData = dataFile.readlines()
        dataFile.close()
        if(hasTitleLine):
            sourceData = sourceData[1:]
        SQLScriptLines = []
        conditionIndexList = conditionColumnNameDict.keys()
        targetIndexList = updateColumnNameDict.keys()
        SQLHead = "update " + tableName + " set "
        for sd in sourceData:
            row = sd
            if(sd[-1] == "\n"):
                row = sd[:-1]
            rowList = row.split(separator)
            SQLBody = ""
            for index in targetIndexList:
                SQLBody = SQLBody + updateColumnNameDict[index] + " = "
                if(updateColumnIsStrDict[index]):
                    SQLBody = SQLBody + "\"" + rowList[index] + "\"" + ","
                else:
                    SQLBody = SQLBody  + rowList[index]  + ","
            SQLBody = SQLBody[:-1]
            SQLTail = " where " 
            for index in conditionIndexList:
                SQLTail = SQLTail + conditionColumnNameDict[index] + " = "
                if(conditionColumnIsStrDict[index]):
                    SQLTail = SQLTail + "\"" + rowList[index] + "\"" + " and "
                else:
                    SQLTail = SQLTail + rowList[index] + " and "
            SQLTail = SQLTail[:-5] + ";\n"
            SQL = SQLHead + SQLBody + SQLTail
            SQLScriptLines.append(SQL)

        SQLFile = open(SQLScriptPath, "w")
        SQLFile.writelines(SQLScriptLines)
        SQLFile.close()

if __name__ == "__main__":
    stu = SQLTransUtils()
    dataFilePath = ""
    hasTitleLine = True
    separator = "\t"
    SQLScriptPath = ""
    tableName = "nodes_table"
    conditionColumnNameDict ={1:""}
    conditionColumnIsStrDict = {1:True}
    updateColumnNameDict = {0:"",4:"",5:""}
    updateColumnIsStrDict = {0:,4:,5:}
    stu.transDataFileToUpdateSQLScript(dataFilePath, SQLScriptPath, tableName, conditionColumnNameDict, conditionColumnIsStrDict, updateColumnNameDict, updateColumnIsStrDict,  hasTitleLine = hasTitleLine, separator = separator)
    SQLScriptPath = ""
    stu.transDataFileToInsertSQLScript(dataFilePath, SQLScriptPath, tableName, updateColumnNameDict, updateColumnIsStrDict, hasTitleLine = hasTitleLine, separator = separator)
    print "Generate fineshed."

