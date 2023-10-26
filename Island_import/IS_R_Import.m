
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


%get the index of specified input variable
name_index = find(strcmp(template_data.Properties.VariableNames, 'dob'));

if ~isempty(name_index)
    % Return the variable in the corresponding second row
    value = template_data{2, name_index};
else
    % Handle the case where 'dob' is not found in the variable names
    error('Variable "dob" not found in the CSV file.');
end




% target_value = 'dob';
% index = find(strcmp(template_data{1, :}, target_value))


% % Write the output data to a CSV file
% writecell(output_data, 'output.csv');

