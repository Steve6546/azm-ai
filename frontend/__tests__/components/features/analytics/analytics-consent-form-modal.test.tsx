import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AnalyticsConsentFormModal } from "#/components/features/analytics/analytics-consent-form-modal";
import AZM AI from "#/api/open-hands";
import { AuthProvider } from "#/context/auth-context";

describe("AnalyticsConsentFormModal", () => {
  it("should call saveUserSettings with consent", async () => {
    const user = userEvent.setup();
    const onCloseMock = vi.fn();
    const saveUserSettingsSpy = vi.spyOn(AZM AI, "saveSettings");

    render(<AnalyticsConsentFormModal onClose={onCloseMock} />, {
      wrapper: ({ children }) => (
        <AuthProvider>
          <QueryClientProvider client={new QueryClient()}>
            {children}
          </QueryClientProvider>
        </AuthProvider>
      ),
    });

    const confirmButton = screen.getByTestId("confirm-preferences");
    await user.click(confirmButton);

    expect(saveUserSettingsSpy).toHaveBeenCalledWith(
      expect.objectContaining({ user_consents_to_analytics: true }),
    );
    await waitFor(() => expect(onCloseMock).toHaveBeenCalled());
  });
});
