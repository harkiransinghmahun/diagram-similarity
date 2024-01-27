# Imports
from calculation.consine_similarity import get_cosine
from calculation.utils import initialise_2d_matrix, print_matrix
from data.sequence_diagram_data import objects_map, object_message_map_1, object_message_map_2, messages_1, messages_2

# Weights
weight_object = 0.2
weight_message = 0.8

weight_object_source = 0.1
weight_class_source = 0.1
weight_method_type = 0.3
weight_method_name = 0.3
weight_object_destination = 0.1
weight_class_destination = 0.1


# Functions
def get_sequence_similarity(seq1, seq2, messages_1, messages_2):
    o_sim = get_object_similarity(objects_map[seq1], objects_map[seq2])
    m_sim = get_message_similarity(messages_1, messages_2)

    seq_sim = weight_object * o_sim + weight_message * m_sim

    return seq_sim


def get_object_similarity(objects_list_1, objects_list_2):
    len_1 = len(objects_list_1)
    len_2 = len(objects_list_2)

    output_matrix = initialise_2d_matrix(len_1, len_2)

    for i in range(len_1):
        for j in range(len_2):
            obj_1 = objects_list_1[i]
            obj_2 = objects_list_2[j]

            output_matrix[i][j] = round(get_object_message_similarity(obj_1, obj_2), 2)

    print_matrix(output_matrix)

    o_sim = 0
    for i in range(len_1):
        max_value = 0
        for j in range(len_2):
            if output_matrix[i][j] > max_value:
                max_value = output_matrix[i][j]
        o_sim += max_value

    o_sim = o_sim/max(len_1, len_2)

    return o_sim


def get_object_message_similarity(obj_1, obj_2):
    mn_1 = object_message_map_1[obj_1]
    mn_2 = object_message_map_2[obj_2]

    max_similarity = []

    for i in range(len(mn_1)):
        max_value = 0
        for j in range(len(mn_2)):
            cosine_sim = get_cosine(mn_1[i].split("_"), mn_2[j].split("_"))
            if cosine_sim > max_value:
                max_value = cosine_sim

        max_similarity.append(max_value)

    if max(len(mn_1), len(mn_2)) == 0:
        return 0

    return sum(max_similarity) / max(len(mn_1), len(mn_2))


def get_message_similarity(messages_1, messages_2):
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

    object_source_1 = msg_1[0].split("_")
    object_source_2 = msg_2[0].split("_")

    class_source_1 = msg_1[1].split("_")
    class_source_2 = msg_2[1].split("_")

    method_type_1 = msg_1[2].split("_")
    method_type_2 = msg_2[2].split("_")

    method_name_1 = msg_1[3].split("_")
    method_name_2 = msg_2[3].split("_")

    object_destination_1 = msg_1[4].split("_")
    object_destination_2 = msg_2[4].split("_")

    class_destination_1 = msg_1[5].split("_")
    class_destination_2 = msg_2[5].split("_")

    msg_sim = (weight_object_source        *  get_cosine(object_source_1, object_source_2)           +
               weight_class_source         *  get_cosine(class_source_1, class_source_2)             +
               weight_method_type          *  get_cosine(method_type_1, method_type_2)               +
               weight_method_name          *  get_cosine(method_name_1, method_name_2)               +
               weight_object_destination   *  get_cosine(object_destination_1, object_destination_2) +
               weight_class_destination    *  get_cosine(class_destination_1, class_destination_2)
               )

    return msg_sim


print("Sequence similarity: " + str(get_sequence_similarity("sq1", "sq2", messages_1, messages_2)))
