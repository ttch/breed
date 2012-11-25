	function {{func_name}}(formData, jqForm, options) {
		clearForm(formData);
		addForm(formData,"StartDate",$('{{field.name}}').val());
	    return true;
	}