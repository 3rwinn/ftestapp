import { Fragment, useEffect } from "react";
import { Transition } from "@headlessui/react";
import { CheckCircleIcon, XCircleIcon } from "@heroicons/react/24/outline";
import { XMarkIcon } from "@heroicons/react/24/solid";
import { useAppContext } from "../context/AppState";

function Notification() {
  const {
    notificationOpen,
    notificationContent,
    switchNotification,
    setNotificationContent,
  } = useAppContext();

  useEffect(() => {
    if (notificationOpen === true) {
      setTimeout(() => {
        setNotificationContent(null);
        switchNotification(false);
      }, 6000);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [notificationOpen]);

  return (
    <>
      {/* Global notification live region, render this permanently at the end of the document */}
      {notificationContent && (
        <div
          aria-live="assertive"
          className="fixed inset-0 z-[1000] flex items-end px-4 py-6 pointer-events-none sm:p-6 sm:items-start"
        >
          <div className="w-full flex flex-col items-start space-y-4 sm:items-end">
            {/* Notification panel, dynamically insert this into the live region when it needs to be displayed */}
            <Transition
              show={notificationOpen}
              as={Fragment}
              enter="transform ease-out duration-300 transition"
              enterFrom="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2"
              enterTo="translate-y-0 opacity-100 sm:translate-x-0"
              leave="transition ease-in duration-100"
              leaveFrom="opacity-100"
              leaveTo="opacity-0"
            >
              <div className="max-w-sm w-full bg-white shadow-lg rounded-lg pointer-events-auto ring-1 ring-black ring-opacity-5 overflow-hidden">
                <div className="p-4">
                  <div className="flex items-start">
                    <div className="flex-shrink-0">
                      {notificationContent.type === "error" ? (
                        <XCircleIcon
                          className="h-6 w-6 text-red-500"
                          aria-hidden="true"
                        />
                      ) : (
                        <CheckCircleIcon
                          className="h-6 w-6 text-green-400"
                          aria-hidden="true"
                        />
                      )}
                    </div>
                    <div className="ml-3 w-0 flex-1 pt-0.5">
                      <p className="text-sm font-medium text-gray-900">
                        {notificationContent.title}
                      </p>
                      <p className="mt-1 text-sm text-gray-500">
                        {notificationContent.description}
                      </p>
                    </div>
                    <div className="ml-4 flex-shrink-0 flex">
                      <button
                        className="bg-white rounded-md inline-flex text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                        onClick={() => {
                          switchNotification(false);
                        }}
                      >
                        <span className="sr-only">Close</span>
                        <XMarkIcon className="h-5 w-5" aria-hidden="true" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </Transition>
          </div>
        </div>
      )}
    </>
  );
}

export default Notification;
