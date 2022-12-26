#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <variant>
#include <vector>

using namespace std;

// string data = "8054F9C95F9C1C973D000D0A79F6635986270B054AE9EE51F8001D395CCFE21042497E4A2F6200E1803B0C20846820043630C1F8A840087C6C8BB1688018395559A30997A8AE60064D17980291734016100622F41F8DC200F4118D3175400E896C068E98016E00790169A600590141EE0062801E8041E800F1A0036C28010402CD3801A60053007928018CA8014400EF2801D359FFA732A000D2623CADE7C907C2C96F5F6992AC440157F002032CE92CE9352AF9F4C0119BDEE93E6F9C55D004E66A8B335445009E1CCCEAFD299AA4C066AB1BD4C5804149C1193EE1967AB7F214CF74752B1E5CEDC02297838C649F6F9138300424B9C34B004A63CCF238A56B71520142A5A7FC672E5E00B080350663B44F1006A2047B8C51CC80286C0055253951F98469F1D86D3C1E600F80021118A124261006E23C7E8260008641A8D51F0C01299EC3F4B6A37CABD80252211221A600BC930D0057B2FAA31CDCEF6B76DADF1666FE2E000FA4905CB7239AFAC0660114B39C9BA492D4EBB180252E472AD6C00BF48C350F9F47D2012B6C014000436284628BE00087C5D8671F27F0C480259C9FE16D1F4B224942B6F39CAF767931CFC36BC800EA4FF9CE0CCE4FCA4600ACCC690DE738D39D006A000087C2A89D0DC401987B136259006AFA00ACA7DBA53EDB31F9F3DBF31900559C00BCCC4936473A639A559BC433EB625404300564D67001F59C8E3172892F498C802B1B0052690A69024F3C95554C0129484C370010196269D071003A079802DE0084E4A53E8CCDC2CA7350ED6549CEC4AC00404D3C30044D1BA78F25EF2CFF28A60084967D9C975003992DF8C240923C45300BE7DAA540E6936194E311802D800D2CB8FC9FA388A84DEFB1CB2CBCBDE9E9C8803A6B00526359F734673F28C367D2DE2F3005256B532D004C40198DF152130803D11211C7550056706E6F3E9D24B0";
string data = "D2FE28";

struct Header {
    Header(const vector<uint8_t>& data, uint64_t& ptr)
    {
        version = (data[ptr / 8] >> (5 - ptr % 8)) & 0b111;
        type = (data[ptr / 8] >> (2 - ptr % 8)) & 0b111;
        ptr += 6;
    }

    unsigned version = 0;
    unsigned type = 0;
};

uint64_t parse_value(const vector<uint8_t>& data, uint64_t& ptr)
{
    bool flag = true;
    uint64_t value = 0;
    for (; flag && ptr < data.size() * 8; ptr++) {
        auto origin = ptr;
        flag = GET_BIT(data, ptr);
        ptr++;
        for (; ptr < origin + 4; ptr++)
            value = (value << 1) | GET_BIT(data, ptr);
    }
    return value;
}

struct Packet {
    Header header;
    union {
        uint64_t value;
    } body;

    Packet(const vector<uint8_t>& data, uint64_t& ptr)
        : header(data, ptr)
    {
        switch (header.type) {
        case 4:
            body.value = parse_value(data, ptr);
            break;
        }
    }
};

int main()
{
    vector<uint8_t> raw;
    vector<Packet> packets;
    for (int i = 0; i < data.length(); i += 2)
        raw.push_back(strtol(&(data.substr(i, 2).data()[i]), nullptr, 16));

    uint64_t ptr = 0;
    while (ptr < raw.size() * 8) {
        packets.emplace_back(raw, ptr);
        // cout << (int)GET_BIT(data, ptr);
        ptr++;

        cout << (unsigned)packets.back().header.type << endl;
    }
}