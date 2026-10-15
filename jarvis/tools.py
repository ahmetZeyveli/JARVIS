import json
from pathlib import Path
from jarvis.config import ROOT_DIRECTORY


# TOOLS_SCHEMAS DeepSeek'e yollanacak olan araç listesidir.
TOOL_SCHEMAS = [
    {
        "type": "function",
         "function": {
             "name": "system_info",
             "description": "Returns basic operation system and platform information. ", #  Temel OS ve platform bilgilerini döner 
             "parameters": {                                                             #  Model araçları çağırırken Python kodunu görerek değil bu açıklamayı okuyarak 
                 "type": "object",                                                       # bu aracı çağıracağına karar verir.
                 "properties": {},
                 "required": []
             },
         },
    },
    {
        "type": "function",
        "function": {
            "name": "write_note",
            "description": "Writes text content into a note file",
            "parameters": {
                "type": "object",
                "propeties": {
                    "note_name": {
                        "type": "string",
                        "description": "The name of the note file",
                    },
                    "content": {
                        "type": "string",
                        "description": "The text content so save",
                    },
                },
                "required": ["note_name","content"],
            },
        },
    },
]
# İmport platfrom ile işletim sisteminin adını, sürümünü ve işlemci mimarisini alıp tek bir metin
# olarak döndürür.
def system_info() -> str:
    import platform
    return f"OS: {platform.system()} {platform.release()}, Machine: {platform.machine()}"

# Dosyayı açar, içine metin yazar ve işi bittiğinde dosyayı bellekte açık bırakmadan otomatik kapatır.
# Config.py' da bulunan ROOT_DIRECTORY ile dosya yolunu bulmayı sağladık.
def write_note(note_name: str, content: str) -> str:

    target_path = (Path(ROOT_DIRECTORY) / note_name).resolve()
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(content, encoding="utf-8")
    return f"Note successfully saved at: {target_path.name}"

#  Model "write_note" u metin olarak gönderdiğinde arka planda if else blokları çalıştırmak yerine
#  sözklükten doğrudan fonksiyonun kendisini çağırabiliriz.
AVAIBLE_TOOLS = {
    "system_info": system_info,
    "write_note": write_note,
}

# Deepseek'ten gelen fonksiyon adı ve argümanları alıp çalıştırır
# Eğer tool name Avaible tools içerisinde değilse json dump ile nedenini açıklar.
def execute_tool(tool_name: str, arguments: dict | str) -> str:
    if tool_name not in AVAIBLE_TOOLS:
        return json.dump(
            {"status": "eror", "message": f"Tool '{tool_name}' not found. "}
        )
    
    # DeepSeek API parametleri Python sözlüğü yada JSON string olarak yollayabilir.
    # Gelen parametrenin metin olup olmadığını kontrol eder. Eğer metin ise Python dictionary'e çevirir.
    # Bozuk bir JSON yollandıysa hatayı yakalar ve yine json.dump ile raporlar.
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments) if arguments.strip() else{}
        except json.JSONDecodeError as error:
            return json.dump(
                {"status": "error", "message": f"Invalid JSON arguments: {error}"}
            )
    # AVAIBLE_TOOLS' tan aranılan fonskiyonu çeker.
    # Sözlüğün içerisindeki veriyi alıp fonksiyona argüman olarak verir.
    # Çalışan fonksiyondan gelen cevabı alır JSON formatında döner.   
    try:
        function_to_call = AVAIBLE_TOOLS[tool_name]
        result = function_to_call(**arguments)
        return json.dumps({"status": "success", "result": result})
    
    #Fonskiyon çalışırken bir hata çıkarsa tüm asistan çökmesin diye hatayı error
    # değişkenine atar ve JSON olarak geri döner.
    except Exception as error:
        return json.dumps(
            {"status": "error", "message": f"Execution failed: {str(error)}"}
        )
