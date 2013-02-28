<style>
.ui-button-icon-only .ui-button-text { padding: 1px; }
.ui-autocomplete {
	max-height: 200px;
	overflow-y: auto;
	/* prevent horizontal scrollbar */
	overflow-x: auto;
	/* add padding to account for vertical scrollbar */
	padding-right: 60;
	max-width : 300px;
}
/* IE 6 doesn't support max-height
 * we use height instead, but this forces the menu to always be this tall
 */
* html .ui-autocomplete {
	height: 200px;
	width : 300px;
}
</style>
