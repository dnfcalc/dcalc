import base64
import zlib
import struct

from core.basic.character import createCharacter
from core.character.adventure import get_adv_info

skill_map = {
    '0': ['65827d506df24a870ef7d2e1aefbfeb7'],
    '1': ['3c5604bdbb0240b8f130f59ab40509c3', '3aacd652747f6729f079bc48747724a4'],
    '2': ['9dda3f4a849dba1a288dd65e116860f2', 'd8ff976e2aaa4720272a5175d1eb9126'],
    '3': ['0969cd4054d93da07708108c0cc1c4b5', 'dacd5c2848a1eb33489e5471f1a73759'],
    '4': ['717f1e2104fe4b796f800352fa143ecc', 'bae12a6dc7d22a5cf149673e88ddda28'],
    '5': ['eb71e1d82d92c7e1d40500a0dcd77aa6', 'c47b66efd27845ef14954928ea2f95c8'],
    '6': ['4655101518604f874721b3cc249aae10', '1c1a9606eb702ebe5a7bb4397f3aeae0'],
    '7': ['56aa7844a2da23f5bea9b585aea5ae45', 'c9664191611af31142e052dfaef84530', '949849d5791944973d60af7e2a7eefb0'],
    '8': ['f2fb27162beb0b87a7cb9af7900e95f2', '96e72ec364dada85600c907ecd95a140'],
    '9': ['cfacda0647b9a0f595df2c2aad30c18d', 'b1ccbd90d0b40f543ece3b18fcef827f'],
    '10': ['2f5d03c7848effbc0a23f4df45d9ca46', '394e2f09c1f37ae61d831d8567707170'],
    '11': ['2ff50c35efcf0f287c4c418c8454da48', '45442bbbe33540b4deeec29437dae70c'],
    '12': ['845e0ce3235e19f60cc82a082d072cba', '01c3a2fb793d293a25ed8dc7a0d70c1a'],
    '13': ['6067de229738524687e5a9ee1c53d583', '8f73f243041c2d27739fe7696f02bf9b'],
    '14': ['33ad4930f4724a7d025c3046c6f6074b', '8c2379737c5acc935c1731f67f607655'],
    '15': ['9ceb0c55f40f1fc0fe0fcc65c8fee3a0', '9cb6f9ed646fa87f9b7680a42ce83d1a'],
    '16': ['aa6dd52e1c925d87cdc0ca340056c543', '4224f9b0b8c7c903e9a1e0f9d9f6d04d'],
    '17': ['78bd107acd474518b606be1e4fd38239', '68062215e75d92575958873ac8ede31a'],
    '18': ['d085127b0edd719782bd618d5688f4a1', '9376d04c476cd41d60ed1974ca69ab95'],
    '19': ['ef9d26746effee9199b54541f01b8752', '42c82812f86ff6704ae9952a2e6093a4'],
    '20': ['3d8f3d438405d79f8d3ed68072674d1e', '5536486eaf9b13c9a8283447cb5e77ab'],
    '21': ['ade01c1d6afc8a05055225045e89fe49', 'dec8961c485edb02036ba00c789010f0'],
    '22': ['ff171dc487807bb9aa28900ca9a46b41', 'e36ae35f8964d92e30e33529a65544d7'],
    '23': ['547ab2b2bd860d3e37355a9cfbc1077c', 'f1fdc6c2482ecc510a2a9f04201ba125'],
    '24': ['506e7ed77d517419a6e1c437a2cedb17', '8e1891ddbdd5ebfcc4508ff2090c3e0f'],
    '25': ['a5fa08f5d509e6ff2ebc68856a470b5a'],
    '26': ['5dc7008b12a459325b548b0715c6b73c', '8c10cefa65364880451e389bb74d3600'],
    '27': ['8ee0099656df08a0b39225f8a21d514b', '38805520deffc10fac2e8f881ab7682b'],
    '28': ['9bff7f2559e003766fee2853dca00631', '66a9967e677651d0def34c475795ccde'],
    '29': ['b69d38bcddd41b3566c6d5cf78d060bb', 'da6e37c1e3f0e8867f70007d89c239ff'],
    '30': ['a6c8f69107f8c4f5d1a0c7a57d000290', '030663e99462f628b4c9f813e1406c4e'],
    '31': ['3829c15bf5f520c13998a3479ba0ce7b', '150aa05b9ee8b9c7c04a25f3e425900c'],
    '32': ['03bb5314ffd41e9458d67ef924fef38f', '89c505581267af77c6d58dc49b710550'],
    '33': ['bb34e8854a93fd250347a1c64119f7ab', 'a81e5b7defa1819263ed8e86f69fd06f'],
    '34': ['1dad88963abdc96b091fcab185a8820d', '89a4529234904fcbb3abe289e281f2fd'],
    '35': ['27bade584bb42fef68148d3a0b72bace', '515b442ffbf61a82371abb645c149a31'],
    '36': ['04883563896fe1adac7505c6146b5f59', '87a918bb22cfc959a16e0bf939bb6c24'],
    '37': ['dcd536f1674630f01fc9667bb202b851', 'aa51c4ddf1659092fa9ed612b9837061'],
    '38': ['762c4e6d030eaf0abbfe1fec2b298574', '863295a0fc634cf5fcc01e82a735fd6b'],
    '39': ['23a5e0fba03283cb1b324a847b3fe370', '3153ca0e6752a6283412c59c5ec8e002'],
    '40': ['0ed3148658fe37b3336ccb718dc0fdb0', '02ac8e048f7bbcfa616e74ac68988872'],
    '41': ['01384bbfc346775d1267fa0bc4ca605f', 'ca2536eb56df0e812c88c59cabd38be0'],
    '42': ['dc1ffbe7bfcc6dc2be737951960da9ad', '7f9ffcd296361f1367b8b74e773d5e99'],
    '43': ['4b2c90ec226fd40e967875aa5eabefb2', 'c1dd8b776fb1dd24c6373c678ef1dd2e'],
    '44': ['e49e57b2e8fbeceb0a2c56a0c63fe6c5', '481348575c1e141925c836b59c5db3ca'],
    '45': ['e4c354a89c337310aeb7041d5e742828', '5f4c55fe2ebdf0623bd76d4fda872ddc'],
    '46': ['fc7a3f4c2852c832a2f20af63d5d212f', '95b58ec89893dd9e50da1281ebe57175'],
    '47': ['128b9ddef2262f40723deae4407bdb42', '573723c8c0614f5b1218ca9ff992115b'],
    '48': ['78be08a3f8c834d3b06fa20c6a08c5a5', 'ebff277c02cc8b54c32635cd0d25f6f3'],
    '49': ['c27418ae613c647527200a7ca17d97fd'],
    '50': ['37cf7b7a269058dc02bef5b5bc9de282', '92360eab6e1f378902018eca681ac629'],
    '51': ['1fadde0eece18649caddbca7bd58cc2f', '97972dba4694d6c0fcd2f7e8efb3a499'],
    '52': ['595908ad107ed3f495329770e9bb9ea5', 'd0cdaca82892e54097f22a1f60817048'],
    '53': ['c381973d97e2e906ea53ba2add33d49c', '1803b6a67047cafb9e289b4f33cc507b'],
    '54': ['4e9e8942841b9767f683fb23c1ef1435', '0232c151ef3731c2dede51931a374723'],
    '55': ['d2c6df5105577fb59fb92529a36165a0', 'ef896bbdc68660c22b6e60502044d690'],
    '56': ['de3fea2d65c597f4d55c70a02b97fc79', '5cf8bfba8b456626deac8bee6f49195f'],
    '57': ['e9a1a1cce5aeaac5414a98a625e7285c', 'c61f5a010370101402b05b21916c2071'],
    '58': ['202edb928046f4fa6dedf6337377efd5'],
    '59': ['f8226512ea3dbcb1fe1374baa0c6bbee', '2a3c96b88d02372505692da0a8b54743'],
    '60': ['bc11d28c04e01923a093d65752c55516', '96c8ddd388e1b08e7fc98c5041382e26'],
    '61': ['a3c4f89a129ebd16896961fd273181e8', 'faf9cd66281078b51be2ee0b0f6c5530'],
    '62': ['1721e94897e9961d5c98130a13392f17'],
    '63': ['ad7405c320c23a1a3430307d4d1b03c0', 'd296043df164385a14cb973c8c7c4d07'],
    '64': ['e2cfb515fe293cf121a649fcc4bab84b'],
    '65': ['6e33d47e6622ce03b6defdd912140270', '7e60ce8aaca12593f889e8551fd1b03a'],
    '66': ['b163d099c8cc27fdb6fd3639c2ee6df9', '05a07505ea102d31540afdb1fbec491f'],
    '67': ['51a08fd0c90f0a5276cd552047fac93d', 'e11831002360a0d4e08c53ff686eea67'],
    '68': ['28b583c75a49103a1d8aabf799c000a4', '3f4ddb4df24a9f78c7778568e80107dd'],
    '69': ['438e291ec31b6b831b0c8e33ff41f138', 'f0cc2c950f3bdf4103c75fa496bcac34'],
    '70': ['b224e3c19599a2496f7470936485e0ad', '147d005ac868e0de52b1f255eea35d62'],
    '71': ['47bd4871f29defc2a0021ee9261d7a5b', '683ecd07d9b89dbe9afee8570a3a828d'],
    '72': ['a988247dfc78c82e364af39ef66e84a0'],
    '73': ['5f75a60c73b72ad60bd4321b96b16662', '8510294202d0e042dd29a2422fc6770d'],
    '74': ['04c7b4361ca81f041e868169ff044252', 'b3659936a9a74c4ed6f7faf07cca1f9e'],
    '75': ['67e7dd8996b5735e788c9420730c077d', '38612d8f2561edc2eb68d5057a837bfa'],
    '76': ['6a1d1f08a6572be420bb3a256c44c015', 'e862146efac2fce3de3a12f038f4116b'],
    '77': ['5f11bba71728448bb64de0dba2b252cf', 'a2d943797daca862a6f321aca6ac9bfa'],
    '78': ['854997c3bdfc3a2b498b4c4001f69e06', 'c7bf7ccab413009640e65ca6f2f0263a'],
    '79': ['61c8cb33dd20b4ff335e8deed70d3d9c', '1b1cfab062e0768bcc889e33e1f30dbf'],
    '80': ['c77a417c43de80c4ce32c1ed405d174a', '38c485cc41f46a7959ae4336325aa45c'],
    '81': ['ecc23c980ea71450c0ad0c3fd232f329', '7a3fc9d473e8ffe21dd900ddf228a437'],
    '82': ['0b8db1e10b3abbd24d38564e708675d5', '94c450d6214cafdc673f763badceeaf1'],
    '83': ['852f8ad797db4dca1405cb3e77198401', 'a99040fc36c75e998aa3ed012b7759c5'],
    '84': ['dcb31a63ef58954f44ff2070c42a9a98', 'b39ccc3dadab9d94569430e39cdf7d60', '56fca6cff74d828e92301a40cd2148b9'],
    '85': ['8572675ec6a1f50b6eff6a867376c2de', '696721534394b40e78ac96e880f19e5a'],
    '86': ['4f2e001e9a19eb7bae50ad1840dfb329', '0dbdeaf846356f8b9380f8fbb8e97377'],
    '87': ['e1f72ce0c2592e738f711345efd8e25d', 'b8f4966608e4ebb3cc80ba4eac3649bb'],
    '88': ['d89f26862e348a801b30bb9fd7125db5', 'd53301bb328baf12a3ae482cc6a565dd', '6166762c62f234c5f50c2d2ebc5e48d0'],
    '89': ['7e904ea3d2a9faa054604e55120a9268', 'd59c9840f65381bde8487757f1753c71'],
    '90': ['dbf8b30c7057032af0d68fcfa289fdae', 'bbc15561bec24f9c1e79e23d715b1dd2'],
    '91': ['5152480fdde81362575a488d4cec4af9', 'de20372767d014d62dc7361ac686834e'],
    '92': ['2391a27457b5a8c6fa4b4670a91bdd11', '3a691a432c58abebc08211df45c4f4bd'],
    '93': ['5892d1fa4462e561ac8f8d2c74892b0a', '25c0018b82c644f6e20d728f1478e671'],
    '94': ['fc458e449ee00b01dbf88d09aae65462', '48d7d6b7617e6ed24027d1478f460c00'],
    '95': ['1812a1ece67bb37b6b44b54766450064', '669f1428193f61f9d92c743b72438c4d', '2ba299855fc22192cba4f73db75e9d0e', '22158115cfe79a15c7369ced0b482646'],
    '96': ['4e62e33aa37394ec4207a72af2968abf'],
    '97': ['34e1bda921012f6018709f1c1a12b04d'],
    '98': ['2c9d9a36c8401bddff6cdb80fab8dc24', 'c591d1827cfbe224031c704e21d07932'],
    '99': ['b89c9ab317bc0a443f6497b7cca2f6a8', 'ca75c965f20a150f99f54155a37400df', '8ad90fd01b5844edd692fff54d9f74e7'],
    '100': ['7cf17936a039b418660424125dc968d7'],
    '101': ['7f80b887a09e88e2c4728c898bd73654'],
    '102': ['e5c09f9132a48dc1d695968592cc5878', 'e1003c1bd2566829cfed17bb4ce8d460'],
    '103': ['af9e4260178303f3f2f267dded09856b', 'e0daa922b19cdc35de879e938361464e', '13a759aad5bb7fb7f08fae8f88c1cdbb'],
    '104': ['b3ba5c678595305d31dcb11a8350971b', '0fbb8de70002ad34f046c94c2cb3e863'],
    '105': ['0495ac9e1153f8a21866c9ba2262cce6', 'c5a2956d8ed3af1746ed2f76ca971a09'],
    '106': ['e0a072e8cef2d77893aad5f68aeed56a', '67f4b84ed61ee86f505a852b202762a0'],
    '107': ['6a949de7a2aaf742b1abfb7872fc85e2', '2a0a39184de92acf1c1375e00b77404c'],
    '108': ['9dc8438e4572d39243c97da31c113acc', 'e52d867ddb2f7acf616611f32cea2b6f'],
    '109': ['c9603b05632f362bb23cae18374e37cf', '3fb8395ae3b81bd608e0c4223a8eb534', '8b08f9504167a9c0f3a1d29d71b7943e'],
    '110': ['5806440d21e7546d50007a5ba11f8024', 'f3d425f6b8186f9b170fd1aab778fa0d', 'c9a29f5c3509b90a96d5ca9b70dc9c85'],
    '111': ['d429147c372b549c3dadcabcba50787f', 'e7e39aa9fcf182c8db543235c8af7dac'],
    '112': ['7ec521d063d2190e1fcc5bd229af9bcf', '14c573777542b4ee3cdca35501b06c97', 'b860cbf5979b4bcc6beea725636b915e'],
    '113': ['0113c8b1306ca76d208f83f2d093dd62', '8d8981a94b8bdd4e3ffad5bc05042080'],
    '114': ['6bbf76bcd2ed3ca25f21b760db4342ad'],
    '115': ['cc9b13baa94dd463477d07ded90e6833', 'ac21c02567f04a92b54dd85c091d1e5a', '653b35b5b59d29daffca47df43b2b0e3'],
    '116': ['ab6fc3303df03b58911967dfca2b5d07', '4b22172f4e00d9735ff44d333a86653d'],
    '117': ['c91a62dc0a18360acf5031ac0ebf09f5', '808a54f780205020087d5818cb5f8559'],
    '118': ['0c3a468aee1f7ce06bf91eb3319518c1'],
    '119': ['5cac3411ccef1af333953e0ded5e942d', '96b90d633d54701fd287421e580268ff', 'a550756080900cb01f29db11ef4f05fa'],
    '120': ['85f7c810ad503790e8626439fe936d56', '832b6196a59cbc1150d167b1b9d91c90'],
    '121': ['002cbdd9bfd0f0b970451ae8d48d029e', 'b95d9f6fc90f067c43da96dc1e861f28'],
    '122': ['31823197cc0b04d4c5dcf8f928d9220c', '50a859dea1a48a2f60916afbfc91434f'],
    '123': ['b4864a42c0ebce383092bf0b0a840a8b', 'dac8d8207618150c162e4c6f9e168527'],
    '124': ['8e358ecf99ac9df31a6132aeafe378a9', '92502df340b3d5410aa3dc46373871a2', 'c39c703f72d289fcd5a8f182068140d4'],
    '125': ['78b86e64fbb74c1db1b71c50a5ac21cd', '28fc502b0b8b4e57709f34a1e9369692'],
    '126': ['f4a561e272cc434a4905b3aa0c0de090', 'ebf367b19fa6d2da41017fd54049f8fa'],
    '127': ['0e409ac3e1c1f3976b3ef2bfe4c13069', '560d1d8b182f750ff020bfd9e0f1aaf4'],
    '128': ['4c5271b0ecce120d7fc113f377fae76f', '6aa32e36149e8299938451f85f9d840a'],
    '129': ['2e2b7efe778656690f9c8cb6e47c3932'],
    '130': ['dde3b443bd5e61d90c34e5ee771e2c28'],
    '131': ['527cdc3ecca985e18ef819d456532b26'],
    '132': ['e788de1a4498c99fcc790302c4d41fed'],
    '133': ['73f7da7230b46b3ff471e00d77e836cf', '902a016f6978f13740f237e4740a5646', 'fa3ee243b36699e9d3fc34328adf6417'],
    '134': ['bdb73ed79f64fbfa8024978ac7f2e0f2', '370586038cf40378f20d338d507a780c'],
    '135': ['86950d7f2717ec59633999187e4a2c16', 'dd32a9825ec1af42a91f2223be6658e5'],
    '136': ['10834437b54f67c4c27f92eaabd59bb1'],
    '137': ['13e8c4ad93473b5fcea11e81ce9456f5', '3b712691fcaaaa80438e5e31b6451884', 'b5e3d014f75f3d17abdea52cca57f7e9'],
    '138': ['efdf4a86b626b8887a145dea6f46a4fe', 'd110449993fb973f1a62c62c695003db'],
    '139': ['8b137fd3943543616513e2b60301b56f', 'b799700ee73e99e0ac27aaa307492033'],
    '140': ['5ece7efb92358406e59338ef66479010', '40b1ffdf0a1b792c2ff9b7f504466c09'],
    '141': ['55a397464db7b3fe3d553432c455a4e6', '5c45f69c9ebc7a784e994369d2cc3c66'],
    '142': ['1e81fd08f9696b9f0165df569e445d08', '4402c6977bf5c9b0d2febe14dc81de6c'],
    '143': ['f1111c21369d2b835b186dd1d58be88d', '96bd070daacc6c1b81d9f24e6d77f48a'],
    '144': ['fa7f1a3dc90600456cbe010e5714bef3'],
    '145': ['5fe93d62fcf6d0b1bb6b910b2dd24a0b', 'b8257acad8c7c379aba91ee63c0bd015'],
    '146': ['2575e479271da5c46990ab0bb88dd677', '9767a375672d9519f6c1c5dff19b7c15'],
    '147': ['a080c9958fc2e4f87d6c55a727eb62b2', 'd58681f38f393dbfd22ffdb049d97002'],
    '148': ['caef38e23a8ae551466f8a8eb039df22', '82fc7ec7cfb2b7afa8c125a2d9420a78'],
    '149': ['4c3e0c5955661f7bbc1ed6a6d3bb7803', '9f57da5cb3651d81ca7dc9f78be33d01'],
    '150': ['0e3da11226dd30c2aaef52e36eff7f3f'],
    '151': ['3cb633d00f8f6ee088682c9171020d26', '8eeca98333667959c403104f6d24da34'],
    '152': ['1bf9711f3f15865e38d7dce51c6b5a8c', '6d7c9a15c08cc41d70125083e869e1a1'],
    '153': ['1ff42548e611b94781a1ae8f063dd679', 'bcbaa4338139bc9342c8a8415dfbe39a'],
    '154': ['3736fe00a26b0086c23db9a4426a5641', '05ee4433394678e5014c67dafee798ff'],
    '155': ['03bd172c9c50cfdcf9d7e83a3ef82842', '29c0b8b3eed7252b3bdcddc2b4e9e3a0'],
    '156': ['dce00e1ce90e34ef5c36ea869ad171bd', 'e0578e280d5de3aa6d59b9ec7498a19b'],
    '157': ['452be74df1c43b4d3080e1b09ed32e08', 'ae7608b87b6e965c6bdd0b3ef4e6d63e'],
    '158': ['f48b0983de6b83180f7d82f0a5882496', '626cfc24770b72b5d7a24c24cda3768b'],
    '159': ['6235960237fdb1b77f2c82b33614dcf4', '7a96c262533919beee21b5a666062880'],
    '160': ['fc30c667a58e1dd54b5d214e04f4f23c'],
    '161': ['d2cc06a46cf7b6020ccc50c30f86ab25'],
    '163': ['9e86a1210874dc2b0c83a4a5a54a7222'],
    '164': ['0db0405a229a667e0ae97108fc5111c4'],
    '165': ['7ccc03c65d676c4d8a7e6a1821409ad0'],
    '166': ['e73e980e87591bc98940afb1ac0fe522'],
    '167': ['b42cab9c815150aee1ef44daec1fe4c5', '50359daccd728ba338d18d9b71ac97e5', 'ca0cc360e00e5f13e33027bf5fc53d5d'],
    '168': ['20b132c5154dbba90372d29e1e5967d7', '1c1cf47273c67ff26eb60b375ace2062'],
    '169': ['7822d6d52e10964a6755f142c666b494', '4e431eaadc1c4563fe33d03c072564f0'],
    '170': ['1c9cf3b27d9d6ee5e024e2592cad24a5', '6b557a0a96ccd83b37ddb77c550f6a68', '2b340542e776818b78f3212af184bd6b'],
    '171': ['1fd827a816f1d00450bcb2cf298a157a'],
    '172': ['68c20fbed9e68d3cb677072c9274736f'],
    '173': ['a8574a8efa365e8e46e805a6e1d7bfef'],
    '175': ['da29a96a20a75aa0cd8fd7f526bdb107', '1fea5a626f15230237946a11a9d11582'],
    '176': ['8403ffaa9106bbfc1fd2e078e54d2e81'],
    '177': ['26a9454eb0d175ebeac162d68814238b'],
    '178': ['a354f4930334e70b0275f5d92668ce3d'],
    '179': ['892ef624d8bf3d7fc045f84825fd6104', '9559c99a9596b20d031de1ce2649b326'],
    '180': ['955eb7e828c2517131a80f580186838c'],
    '181': ['c6eaf15c287d9154479d1714cad5b4e0'],
    '182': ['6bdcefb90e5e4387d4faa3633b4b587c'],
    '183': ['5fed75723a5d5d373c9f54fba1c7dc06'],
    '184': ['56ef36c1980e67dd2bb50b180a925b89'],
    '185': ['d40a932ac818bf4fa044dc1e4f8b2708'],
    '186': ['fc1262c19f3d0477ee8eda47b8db8696'],
    '190': ['12dca7fbf791e882b025a0d916181673', 'ce26c6b69d02a440a81b552bec94f03b'],
    '198': ['7dd85dccf7ae1f65609c36d66e2e1c95'],
    '199': ['ce572b597666f4472b1577a02fd5e1c3'],
    '222': ['1f4b87944dc5551b91bf6cd25d84b48e'],
    '228': ['a3880ba488ddca966c36c640cce927a7'],
    '229': ['b306cc4c67c775ab7ddff9785a3fe6a4'],
    '231': ['2b39a776471c142f581ad3cc8bb89e55'],
    '232': ['2e9c5a06ff3fe8aea672a2a55c40fdbf'],
    '233': ['374f53e8989ef04a8506c8ec99d9ecdc'],
    '234': ['e1daab884dd07fc9e70d08b83d1790eb'],
    '235': ['b501ae53638d33a32351904f31cb6aa3'],
    '236': ['0c262dac3ec41ff79e359ada9c7a7faf'],
    '237': ['8ec9da6f808889b63adf2680fbf1f331'],
    '238': ['c524c4f378d1cd0ff99e4580750a4567'],
    '239': ['3af805da8505fe6234a95b535610f064'],
    '240': ['c4a5b868f1e8e60cd1867a2cfab4a242'],
    '241': ['8d996a242c5c0efd8cfe6cb4bc6defcc'],
    '242': ['9bc30e0f6e22b0333762d04acae7d252'],
    '243': ['087d1068ff506d090710566608a17760'],
    '244': ['95103ae7c54eaedea3bbcf726520db6c'],
    '246': ['0fc47245af1f21c3e9217d03aa9fff0a'],
    '247': ['328867949b763ce73e243da84fd59157'],
    '248': ['5197b141332a65a89d452adf227c2f30'],
    '249': ['75747c67e14eec6088ce67f63ea41628'],
    '250': ['ce7cd04a44e32212e80f120f4421996e'],
    '251': ['f45301a5590cccefbe0becf2f8d029f5'],
    '252': ['5c00ce6d7dbbb5e9a0f6e1071d486832'],
    '253': ['b1732acfaf117f8e9ff130f47d3ed0e7'],
    '255': ['d204ec03a0aed2f20211fb6ccc48d46d'],
}

role_map = {
    # swordman_male
    '0': 0,
    # fighter_female
    '1': 3,
    # gunner_male
    '2': 4,
    # mage_female
    '3': 7,
    # priest_male
    '4': 8,
    # gunner_female
    '5': 5,
    # thief
    '6': 10,
    # fighter_male
    '7': 2,
    # mage_male
    '8': 6,
    # 黑暗武士
    '9': 15,
    # 缔造者
    '10': 15,
    # swordman_female
    '11': 1,
    # knight
    '12': 11,
    # demonic_lancer
    '13': 12,
    # priest_female
    '14': 9,
    # gunblader
    '15': 13,
    # archer
    '16': 14,
}


def decode_skill_hash(encoded: str) -> dict:
    """
    解码 DNF 技能加点编码。

    编码流程: base64 -> zlib decompress -> 二进制
    二进制结构:
      [0xF3] [Header 14B] [UTF-16LE 角色名]
      [Section1: N个(技能索引,等级)对]
      [Section2: 进化 | 强化 | 键位 | 其他]
      [零填充] [0xF3]

    Section1 中每个 uint16 的高字节=数据值，低字节=标志位。
    Section2 按字节读取，包含三部分定长子结构。
    """
    raw = zlib.decompress(base64.b64decode(encoded))
    header = _parse_header(raw)

    data = raw[14 + header['name_byte_len'] :]
    if len(data) % 2:
        data += b'\x00'

    uint16s = [struct.unpack_from('<H', data, i)[0] for i in range(0, len(data), 2)]
    high = [v >> 8 for v in uint16s]
    low = [v & 0xFF for v in uint16s]

    num_pairs = high[0]
    skills = []
    for p in range(num_pairs):
        i = 1 + p * 2
        if i + 1 >= len(high):
            break
        skills.append(
            {
                'skill_index': high[i],
                'level': high[i + 1],
                'skill_flag': low[i],
                # 0 被动 1 主动
                'skill_type': low[i + 1],
            }
        )

    sec2_bytes = data[(1 + num_pairs * 2) * 2 :]
    evolutions, enhancements, keybinds, remaining = _parse_section2(sec2_bytes)

    return {
        'header': header,
        'skills': skills,
        'evolutions': evolutions,
        'enhancements': enhancements,
        'keybinds': keybinds,
        'section2_remaining': remaining,
        'raw_size': len(raw),
    }


def _parse_header(raw: bytes) -> dict:
    nlen = raw[13]
    return {
        'magic': raw[0],
        'version': raw[1],
        'job_bytes': (raw[2], raw[3]),
        'level': raw[5],
        'job_marker': chr(raw[8]),
        'name': raw[14 : 14 + nlen].decode('utf-16-le'),
        'name_byte_len': nlen,
    }


def _parse_section2(sec2: bytes):
    """
    Section2 子结构:
      byte[0]:  标记位
      byte[1]:  进化数量 E
      byte[2..2+3E-1]:  E 个进化条目，每条 3 字节 (技能索引, 标志, 类型-1)
      byte[2+3E]:  强化数量 H
      byte[2+3E+1..2+3E+3H]:  H 个强化条目，每条 3 字节
      byte[2+3E+3H+1]:  键位数量 K (固定 0x0E=14)
      byte[..+2K]:  K 个键位条目，每条 2 字节 (技能索引, 标志)
      剩余: 其他数据
    """
    if len(sec2) < 2:
        return [], [], [], sec2

    off = 0
    off += 1  # byte[0]: marker

    evo_count = sec2[off]
    off += 1
    evolutions = []
    for _ in range(evo_count):
        if off + 3 > len(sec2):
            break
        evolutions.append(
            {
                'skill_index': sec2[off],
                'flag': sec2[off + 1],
                'type': sec2[off + 2] + 1,
            }
        )
        off += 3

    if off >= len(sec2):
        return evolutions, [], [], b''

    enh_count = sec2[off]
    off += 1
    enhancements = []
    for _ in range(enh_count):
        if off + 3 > len(sec2):
            break
        enhancements.append(
            {
                'skill_index': sec2[off],
                'flag': sec2[off + 1],
                'type': sec2[off + 2] + 1,
            }
        )
        off += 3

    if off >= len(sec2):
        return evolutions, enhancements, [], b''

    key_count = sec2[off]
    off += 1
    keybinds = []
    for slot in range(key_count):
        if off + 2 > len(sec2):
            break
        idx = sec2[off]
        flag = sec2[off + 1]
        keybinds.append(
            {
                'slot': slot,
                'skill_index': idx if idx != 0 else None,
                'flag': flag,
            }
        )
        off += 2

    remaining = sec2[off:]
    return evolutions, enhancements, keybinds, remaining


def get_skill_tree_info(encoded: str) -> dict:
    r = decode_skill_hash(encoded)
    header = r['header']
    role = role_map.get(str(header['job_bytes'][0]), None)
    job_id = int(header['job_bytes'][1]) - 1
    # 黑暗武士
    if header['job_bytes'][0] == 9:
        job_id = 1
    # 缔造者
    if header['job_bytes'][0] == 10:
        job_id = 0
    id = base64.b64encode(f'{role:02}{job_id:02}00'.encode()).decode()
    advInfo = get_adv_info(id)
    className = advInfo['class']
    character = createCharacter(className)
    skillMap = {}
    for index, i in enumerate(r['skills']):
        skillIndex = i['skill_index']
        skillUuids = skill_map.get(str(skillIndex), [None])
        skills = []
        for uuid in skillUuids:
            skill = next((s for s in character.skills if s.uuid == uuid), None)
            if skill is not None:
                skills.append(skill)
        skillMap[skillIndex] = skills
        if len(skills) == 0:
            r['skills'][index] = None
    for k, v in skillMap.items():
        if len(v) > 1:
            skillMap[k] = [s for s in v if s.learnLv not in [50, 85]]
    skillLearn = {}
    # 处理技能等级
    for skill in r['skills']:
      if skill is None:
        continue
      skillIndex = skill['skill_index']
      candidates = skillMap.get(skillIndex, [])
      chosen = None
      if len(candidates) == 1:
        chosen = candidates[0]
      elif len(candidates) > 1:
        chosen = next((x for x in candidates if x.type == ('active' if skill['skill_type'] == 1 else 'passive')), None)
      if chosen and skillLearn.get(str(chosen.id), {'lv': 0})['lv'] < skill['level']:
        skillLearn[str(chosen.id)] = {
          'lv': skill['level'],
          'up': 0,
          'vp': 0,
          'name': chosen.name,
        }
    # 处理进化
    for evo in r['evolutions']:
      for s in skillMap.get(evo['skill_index'], []):
        if getattr(s, 'hasVP', False) and str(s.id) in skillLearn:
          skillLearn[str(s.id)]['vp'] = evo['type']

    # 处理强化
    for enh in r['enhancements']:
      for s in skillMap.get(enh['skill_index'], []):
        if getattr(s, 'hasUP', False) and str(s.id) in skillLearn:
          skillLearn[str(s.id)]['up'] = enh['type']
    for i in character.skills:
       if str(i.id) not in skillLearn:
          skillLearn[str(i.id)] = {
          'lv': i.calculate_lv() if (i.learnLv in [50,85] or i.name == '基础精通') and str(i.id) else 0,
          'up': 0,
          'vp': 0,
          'name': i.name,
        }
    return {
       "name": header['name'],
       "level": header['level'],
       "job":advInfo,
       "skills": skillLearn
    }


# def print_decoded(encoded: str):
#     """解码并打印技能编码的全部信息。"""
#     r = decode_skill_hash(encoded)
#     h = r['header']

#     print('=' * 70)
#     print('DNF 技能加点编码解析')
#     print('=' * 70)

#     print(f'\n【角色信息】')
#     print(f'  角色名:     {h["name"]}')
#     print(f'  等级:       {h["level"]}')
#     print(f'  职业字节:   ({int(h["job_bytes"][0])}, {int(h["job_bytes"][1])})')
#     print(f'  编码版本:   {h["version"]}')
#     print(f'  数据大小:   {r["raw_size"]} bytes')

#     print(f'\n  主动投入技能 (等级 > 1):')
#     for s in reversed(r['skills']):
#         f = ''
#         if s['skill_flag']:
#             f += f' sf={s["skill_flag"]}'
#         if s['level_flag']:
#             f += f' lf={s["level_flag"]}'
#         print(f'    技能 {int(s["skill_index"]):<5d}  Lv.{s["level"]:<3d}{f}')

#     print(f'\n【进化选择】({len(r["evolutions"])} 个)')
#     for e in r['evolutions']:
#         t = '选项一' if e['type'] == 1 else '选项二'
#         print(f'    技能 {int(e["skill_index"]):<5d}  {t}')

#     print(f'\n【强化选择】({len(r["enhancements"])} 个)')
#     for e in r['enhancements']:
#         t = f'类型{e["type"]}'
#         print(f'    技能 {int(e["skill_index"]):<5d}  {t}')

#     active = [k for k in r['keybinds'] if k['skill_index'] is not None]
#     print(f'\n【快捷键】({len(active)}/{len(r["keybinds"])} 槽位已使用)')
#     for k in r['keybinds']:
#         if k['skill_index'] is not None:
#             f = f' (flag={k["flag"]})' if k['flag'] else ''
#             print(f'    槽位 {k["slot"]:2d}: 技能 {int(k["skill_index"]):<5d}{f}')
#         else:
#             print(f'    槽位 {k["slot"]:2d}: (空)')
