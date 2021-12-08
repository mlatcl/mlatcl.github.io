function printJS(jsObject) {
    console.log(JSON.stringify(jsObject, null, 2));
}

const dblp = new DBLP();

async function extractInfo() {
    var tiago_json = await dblp.getByPID('188/5658');
    printJS(tiago_json.getJSON());
}

extractInfo();