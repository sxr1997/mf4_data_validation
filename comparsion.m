clc;

origin_file = "LOGS\HONDA_SRR6+___20240704___SW11FFF5_COT_001.mf4";
merged_file = "LOGS\merged_data\HONDA_SRR6+___20240704___SW11FFF5_COT_001_ORCAS.mf4";

%fileInfo = mdfInfo(origin_file);
%data_origin = mdfRead(origin_file);
%data_merged = mdfRead(merged_file);

file_path = '.\LOGS\';
file_type = '*.mf4';
original_file = dir([file_path file_type]);
original_filename = {original_file.name}';
Length = size(original_filename,1);
for i = 1 : Length
    res(i) = original_filename(i);
    file_list(i) = strcat(file_path, '\', res(i));
end
file_list = file_list';
timestamps_origin_total = 0;
for i = 1 : Length
    timestamps = mdfChannelInfo(file_list(i), Channel="TimeStamp");
    timestamps_origin_total = timestamps_origin_total + timestamps(1, 3);
end
timestamps_origin_total
timestamps_merged = mdfChannelInfo(merged_file, Channel="TimeStamp")