
#!/bin/bash

# 要转换的HDR文件所在的目录
directory="/home/wxy/Documents/hdrimages"

# 遍历目录中的每个HDR文件并转换为HTML文件
for hdr_file in "$directory"/*.hdr; do
    if [ -f "$hdr_file" ]; then
        # 提取文件名（不包括路径和扩展名）
        filename=$(basename "$hdr_file" .hdr)
        pfsin "$hdr_file"|pfsouthdrhtml
        # 调用pfsouthdrhtml命令转换为HTML文件
        
    fi
done


