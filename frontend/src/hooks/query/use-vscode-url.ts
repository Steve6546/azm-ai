import { useQuery } from "@tanstack/react-query";
import AZM AI from "#/api/open-hands";
import { useConversation } from "#/context/conversation-context";

export const useVSCodeUrl = (config: { enabled: boolean }) => {
  const { conversationId } = useConversation();

  const data = useQuery({
    queryKey: ["vscode_url", conversationId],
    queryFn: () => {
      if (!conversationId) throw new Error("No conversation ID");
      return AZM AI.getVSCodeUrl(conversationId);
    },
    enabled: !!conversationId && config.enabled,
    refetchOnMount: true,
  });

  return data;
};
