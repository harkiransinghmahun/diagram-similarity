# Imports
from calculation.consine_similarity import get_cosine
from calculation.utils import initialise_2d_matrix, print_matrix
from data.orders_workflow_data import client_workflow_map, client_workflow_message_map, client_message_map

# Weights
weight_workflow = 0.2
weight_messages = 0.8

weight_source = 0.1
weight_msg_type = 0.8
weight_destination = 0.1


# Functions
def get_sequence_similarity(client_1, client_2, client_workflow_map, client_workflow_message_map, client_message_map):

    o_sim = get_client_workflow_similarity(client_1, client_2, client_workflow_map, client_workflow_message_map)
    m_sim = get_message_similarity(client_1, client_2, client_message_map)

    seq_sim = weight_workflow * o_sim + weight_messages * m_sim

    return seq_sim


def get_client_workflow_similarity(client_1, client_2, client_workflow_map, client_message_map):

    client_1_workflow_list = client_workflow_map[client_1]
    client_2_workflow_list = client_workflow_map[client_2]

    client_1_workflow_message_map = client_message_map[client_1]
    client_2_workflow_message_map = client_message_map[client_2]

    client_1_workflow_len = len(client_1_workflow_list)
    client_2_workflow_len = len(client_2_workflow_list)

    output_matrix = initialise_2d_matrix(client_1_workflow_len, client_2_workflow_len)

    for i in range(client_1_workflow_len):
        for j in range(client_2_workflow_len):
            workflow_name_1 = client_1_workflow_list[i]
            workflow_name_2 = client_2_workflow_list[j]

            output_matrix[i][j] = round(get_workflow_message_similarity(workflow_name_1, workflow_name_2, client_1_workflow_message_map, client_2_workflow_message_map), 2)

    print_matrix(output_matrix)

    sim = 0
    for i in range(client_1_workflow_len):
        max_value = 0
        for j in range(client_2_workflow_len):
            if output_matrix[i][j] > max_value:
                max_value = output_matrix[i][j]
        sim += max_value

    sim = sim/max(client_1_workflow_len, client_2_workflow_len)

    return sim


def get_workflow_message_similarity(workflow_name_1, workflow_name_2, client_1_workflow_message_map, client_2_workflow_message_map):
    message_list_1 = client_1_workflow_message_map[workflow_name_1]
    message_list_2 = client_2_workflow_message_map[workflow_name_2]

    max_similarity = []

    for i in range(len(message_list_1)):
        max_value = 0
        for j in range(len(message_list_2)):
            cosine_sim = get_cosine(message_list_1[i].split("_"), message_list_2[j].split("_"))
            if cosine_sim > max_value:
                max_value = cosine_sim

        max_similarity.append(max_value)

    return sum(max_similarity) / max(len(message_list_1), len(message_list_2))


def get_message_similarity(client_1, client_2, client_message_map):
    messages_1 = client_message_map[client_1]
    messages_2 = client_message_map[client_2]

    m_len_1 = len(messages_1)
    m_len_2 = len(messages_2)

    output_matrix = initialise_2d_matrix(m_len_1, m_len_2)

    for i in range(m_len_1):

        for j in range(m_len_2):
            msg_1 = messages_1[i]
            msg_2 = messages_2[j]

            output_matrix[i][j] = round(compute_message_similarity(msg_1, msg_2), 2)

    print_matrix(output_matrix)

    m_sim = 0
    for i in range(m_len_1):
        max_value = 0
        for j in range(m_len_2):
            if output_matrix[i][j] > max_value:
                max_value = output_matrix[i][j]
        m_sim += max_value

    m_sim = m_sim / max(m_len_1, m_len_2)

    return m_sim


def compute_message_similarity(msg_1, msg_2):

    source_1 = msg_1[0].split("_")
    source_2 = msg_2[0].split("_")

    msg_type_1 = msg_1[1].split("_")
    msg_type_2 = msg_2[1].split("_")

    destination_1 = msg_1[2].split("_")
    destination_2 = msg_2[2].split("_")


    msg_sim = (weight_source       *  get_cosine(source_1, source_2)           +
               weight_msg_type     *  get_cosine(msg_type_1, msg_type_2)       +
               weight_destination  *  get_cosine(destination_1, destination_2)
               )

    return msg_sim


def main():
    client_1 = "ntex"
    client_2 = "ubs"
    print("Sequence Similarity: " + str(get_sequence_similarity(client_1, client_2, client_workflow_map, client_workflow_message_map, client_message_map)))


if __name__ == "__main__":
    main()
