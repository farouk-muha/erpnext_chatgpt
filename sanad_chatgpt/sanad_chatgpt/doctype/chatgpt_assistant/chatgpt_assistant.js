// Copyright (c) 2023, Farouk Muharram and contributors
// For license information, please see license.txt

frappe.ui.form.on('ChatGPT Assistant', {
	// refresh: function(frm) {

	// }
	send: function(frm) {
		if(frm.doc.api_key && frm.doc.question){
			frappe.call({
				method: "sanad_chatgpt.sanad_chatgpt.doctype.chatgpt_assistant.chatgpt_assistant.get_chat_response",
				args: {"api_key": frm.doc.api_key, "input_text": frm.doc.question},
				freeze:true,
				callback: function(r) {
					if (r.message.message.content){
						frm.set_value("answer", r.message.message.content);
					}
					
				}
			});
		}else{
			frappe.msgprint("please, enter API Key and Question first!");
		}
	},
});
