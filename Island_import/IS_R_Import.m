
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
input_filename = "input.csv";
input_data = readtable(input_filename);

%REORDER COLUMNS
output_columns = {template_data(1,:)}
input_data = input_data(:, output_columns)


%READING THE TEMPLATE
template_filename = "template.csv";
template_data =  readcell(template_filename);

%GENERATING THE OUTPUT
%setting the first row of output to = the first row of the template
output_data = template_data(1,:);

%get the index of specified input variable
name_index = find(strcmp(input_data(1, :), 'dob'));
%return the variable in the corresponding second row
value = input_data{2,name_index};




% Write the output data to a CSV file
writecell(output_data, 'output.csv');

