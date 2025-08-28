

import os
import os
def get_extention(text):
    text = text.replace("create", "").strip()

    if "python file" in text:
        ex = ".py"
    elif "java file" in text:
        ex = ".java"
    elif "text file" in text:
        ex = ".txt"
    elif "html file" in text:
        ex = ".html"
    elif "css file" in text:
        ex = ".css"
    elif "javascript file" in text:
        ex = ".js"
    elif "c file" in text:
        ex = ".c"
    elif "cpp file" in text:
        ex = ".cpp"
    elif "json file" in text:
        ex = ".json"
    elif "xml file" in text:
        ex = ".xml"
    elif "yaml file" in text:
        ex = ".yaml"
    elif "markdown file" in text:
        ex = ".md"
    elif "csv file" in text:
        ex = ".csv"
    elif "ts file" in text:
        ex = ".ts"
    elif "sql file" in text:
        ex = ".sql"
    elif "log file" in text:
        ex = ".log"
    elif "pdf file" in text:
        ex = ".pdf"
    elif "worf file" in text:
        ex = ".docx"
    elif "powerpoint file" in text:
        ex = ".pptx"
    elif "tar file" in text:
        ex = ".tar"
    else:
        pass
    return ex    


def update_text(text):
    text = text.replace("create", "").strip()

    if "python file" in text:
        text = text.replace("python file", "")
    elif "java file" in text:
        text = text.replace("java file", "")
    elif "text file" in text:
        text = text.replace("text file", "")
    elif "html file" in text:
        text = text.replace("html file", "")
    elif "css file" in text:
        text = text.replace("css file", "")
    elif "javascript file" in text:
        text = text.replace("javascript file", "")
    elif "c file" in text:
        text = text.replace("c file", "")
    elif "cpp file" in text:
        text = text.replace("cpp file", "")
    elif "json file" in text:
        text = text.replace("json file", "")
    elif "xml file" in text:
        text = text.replace("xml file", "")
    elif "yaml file" in text:
        text = text.replace("yaml file", "")
    elif "markdown file" in text:
        text = text.replace("markdown file", "")
    elif "csv file" in text:
        text = text.replace("csv file", "")
    elif "ts file" in text:
        text = text.replace("ts file", "")
    elif "sql file" in text:
        text = text.replace("sql file", "")
    elif "log file" in text:
        text = text.replace("log file", "")
    elif "pdf file" in text:
        text = text.replace("pdf file", "")
    elif "worf file" in text:
        text = text.replace("word file","")
    elif "powerpoint file" in text:
        text = text.replace("powerpoint file", "")
    elif "tar file" in text:
        text = text.replace("tar file", "")
    else:
        pass
    return text 

def create_File(text):
    selected_ex = get_extention(text)
    text = update_text(text)
    if "named" in text or "with name" in text:
        text = text.replace("named","")
        text = text.replace("create", "")
        text = text.replace("with name", "")
        text = text.strip()
        with open(f"{text}{selected_ex}","w"):
            pass

    else:
        with open(f"demo{selected_ex}","w"):
            pass

  