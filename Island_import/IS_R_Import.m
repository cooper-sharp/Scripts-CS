
%generate tania_subid
fn = 'Avi';
ln = 'Dachs';
dob = '10/02/2002';
%get the first letter of their first and last names
fn_letter = fn(1);
ln_letter = ln(1);
%convert letters to corresponding number value
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
fn_num = strfind(alphabet,fn_letter);
ln_num = strfind(alphabet,ln_letter);
%pad the numbers with 0
fn_padded_num = sprintf('%02d', fn_num);
ln_padded_num = sprintf('%02d', ln_num);
%get the last two digits of their dob
dob_num = dob(end-1:end);
%bippity boppity boo
tania_subid = [fn_padded_num, ln_padded_num, dob_num];


%READING THE INPUT
input_data = readtable("/Users/avidachs/Documents/GitHub/Scripts-CS/Island_import/input.csv");

%READING THE TEMPLATE
template_file = "/Users/avidachs/Documents/GitHub/Scripts-CS/Island_import/template.csv";
template_data =  readtable(template_file);




% Extract the variable names from the first row of template_data
templateVarNames = template_data.Properties.VariableNames;

% Initialize an empty cell array for the data
outputDataCell = cell(1, numel(templateVarNames));

% Loop through the variable names and copy data from input_data if it exists
for i = 1:numel(templateVarNames)
    varName = templateVarNames{i};
    if ismember(varName, input_data.Properties.VariableNames)
        outputDataCell{i} = input_data{1, varName};
    else
        outputDataCell{i} = NaN; % Or any other default value
    end
end

% Create the output_data table with the variable names from template_data
% and data from input_data (where they match)
output_data = cell2table(outputDataCell, 'VariableNames', templateVarNames);

writetable(output_data, 'output.csv')

